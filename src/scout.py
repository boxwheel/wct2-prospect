"""
Prospect scouting script for wct2 campaign.
Explores data fields to assess hypothesis feasibility.
Run: python src/scout.py
"""
import pandas as pd
import numpy as np
import re
import json
from pathlib import Path

DATA = Path('/home/user/research/data/wct2')

def load_data():
    pm = pd.read_csv(DATA / 'piterfm/matches_1930_2022.csv')
    wcp = pd.read_csv(DATA / 'abecklas/WorldCupPlayers.csv')
    wcm = pd.read_csv(DATA / 'abecklas/WorldCupMatches.csv')
    wct = pd.read_csv(DATA / 'abecklas/WorldCups.csv')
    pwc = pd.read_csv(DATA / 'piterfm/world_cup.csv')
    return pm, wcp, wcm, wct, pwc

def compute_feasibility_stats(pm, wcp, wcm, wct, pwc):
    stats = {}

    # 1. xG coverage
    stats['xg_coverage'] = {
        'years': [2018, 2022],
        'n_matches': int(pm['home_xg'].notna().sum()),
        'total_matches': len(pm)
    }

    # 2. Own goal asymmetry
    og_home = (pm['home_own_goal'].notna() &
               (pm['home_own_goal'].astype(str).str.strip() != '') &
               (pm['home_own_goal'].astype(str).str.strip() != 'nan'))
    og_away = (pm['away_own_goal'].notna() &
               (pm['away_own_goal'].astype(str).str.strip() != '') &
               (pm['away_own_goal'].astype(str).str.strip() != 'nan'))
    stats['own_goals'] = {
        'home': int(og_home.sum()),
        'away': int(og_away.sum()),
        'ratio': round(og_home.sum() / og_away.sum(), 2),
        'total_matches': len(pm)
    }

    # 3. Goal timing (WorldCupPlayers)
    def parse_goal_mins(s):
        if pd.isna(s): return []
        return [int(m) for m in re.findall(r'G(\d+)', s)]
    wcp['goal_mins'] = wcp['Event'].apply(parse_goal_mins)
    all_mins = []
    for m in wcp['goal_mins']: all_mins.extend(m)
    all_mins = pd.Series(all_mins)
    bins = [0,15,30,45,60,75,90,150]
    labels = ['1-15','16-30','31-45','46-60','61-75','76-90','91+']
    dist = pd.cut(all_mins, bins=bins, labels=labels).value_counts().sort_index()
    stats['goal_timing'] = {
        'total_goals': len(all_mins),
        'dataset': 'WorldCupPlayers (abecklas 1930-2014)',
        'distribution': dist.to_dict()
    }

    # 4. Penalty shootouts
    pen = pm[pm['Notes'].notna() & pm['Notes'].str.contains('penalty kicks', na=False)]
    pen_home_wins = pen.apply(lambda r: r['home_team'] in r['Notes'], axis=1)
    stats['penalty_shootouts'] = {
        'n_shootouts': len(pen),
        'home_wins': int(pen_home_wins.sum()),
        'home_win_pct': round(pen_home_wins.mean() * 100, 1)
    }

    # 5. Golden Boot vs Champion
    golden_boot_from_champion = 0
    gb_details = []
    for _, row in pwc.iterrows():
        champ = row['Champion']
        ts = row['TopScorrer']
        # Known matches: 1978 Kempes/Argentina, 1982 Rossi/Italy, 2002 Ronaldo/Brazil
        match = False
        if row['Year'] == 1978 and 'Kempes' in ts: match = True
        if row['Year'] == 1982 and 'Rossi' in ts: match = True
        if row['Year'] == 2002 and 'Ronaldo' in ts: match = True
        if match: golden_boot_from_champion += 1
        gb_details.append({'year': row['Year'], 'champion': champ, 'top_scorer': ts, 'match': match})
    stats['golden_boot'] = {
        'n_tournaments': len(pwc),
        'golden_boot_from_champion': golden_boot_from_champion,
        'pct': round(golden_boot_from_champion / len(pwc) * 100, 1),
        'details': gb_details
    }

    # 6. Extra time matches
    et = pm[pm['Notes'].notna() & pm['Notes'].str.contains('Extra Time|extra time|penalty kicks', na=False)]
    stats['extra_time'] = {
        'n_matches': len(et),
        'total_matches': len(pm),
        'pct': round(len(et) / len(pm) * 100, 1)
    }

    # 7. Champions with group stage losses (abecklas covers 1930-2014)
    wct_champions = wct[['Year', 'Winner']].copy()
    pwc_champs_extra = pwc[pwc['Year'].isin([2018, 2022])][['Year', 'Champion']].rename(columns={'Champion': 'Winner'})
    all_champs = pd.concat([wct_champions, pwc_champs_extra], ignore_index=True)

    champ_losses = []
    wcm_clean = wcm.dropna(subset=['Home Team Name', 'Away Team Name', 'Home Team Goals', 'Away Team Goals'])
    wcm_clean = wcm_clean.copy()
    wcm_clean['Year'] = wcm_clean['Year'].astype(int)

    for _, row in all_champs.iterrows():
        year, winner = int(row['Year']), row['Winner']
        if year <= 2014:
            yr_matches = wcm_clean[wcm_clean['Year'] == year]
            champ_m = yr_matches[(yr_matches['Home Team Name'] == winner) |
                                  (yr_matches['Away Team Name'] == winner)]
            grp_m = champ_m[champ_m['Stage'].str.contains('Group|First round|Preliminary', na=False, case=False)]
        else:
            pm_grp = pm[(pm['Year'] == year) &
                        (pm['Round'].str.contains('Group|First round', na=False, case=False))]
            grp_m = pm_grp[(pm_grp['home_team'] == winner) | (pm_grp['away_team'] == winner)]

        losses = 0
        for _, m in grp_m.iterrows():
            if year <= 2014:
                if m['Home Team Name'] == winner:
                    gf, ga = m['Home Team Goals'], m['Away Team Goals']
                else:
                    gf, ga = m['Away Team Goals'], m['Home Team Goals']
            else:
                if m['home_team'] == winner:
                    gf, ga = m['home_score'], m['away_score']
                else:
                    gf, ga = m['away_score'], m['home_score']
            if gf < ga:
                losses += 1
        champ_losses.append({'year': year, 'champion': winner, 'group_losses': losses})

    total_with_loss = sum(1 for c in champ_losses if c['group_losses'] > 0)
    stats['champion_group_losses'] = {
        'n_tournaments': len(champ_losses),
        'champions_with_group_loss': total_with_loss,
        'pct': round(total_with_loss / len(champ_losses) * 100, 1),
        'details': champ_losses
    }

    return stats

if __name__ == '__main__':
    pm, wcp, wcm, wct, pwc = load_data()
    stats = compute_feasibility_stats(pm, wcp, wcm, wct, pwc)
    out = Path('artifacts/feasibility_stats.json')
    out.parent.mkdir(exist_ok=True)
    with open(out, 'w') as f:
        json.dump(stats, f, indent=2)
    print("Feasibility stats written to artifacts/feasibility_stats.json")
    for k, v in stats.items():
        print(f"\n{k}:", json.dumps(v, indent=2)[:500])
