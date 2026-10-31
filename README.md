# 2026 FIFA World Cup — Midfield Scouting \& Recruitment Analysis

## Project Overview

This project addresses a football recruitment problem with two primary objectives:

1. **Identify elite midfielders** from the 2026 FIFA World Cup based on their statistical performance and overall impact.
2. **Identify the most cost-efficient recruitment options** among those elite midfielders, helping a football club prioritise players who offer strong performance relative to their estimated market value.

Rather than evaluating midfielders as one general group, the project examines their suitability across three broad midfield roles: Attacking Midfielder (AMF), Box-to-Box Midfielder (B2B), and Defensive Midfielder (DMF).

The analysis combines player statistics, role-specific performance scoring, recruitment shortlisting and estimated market-value comparisons to produce a data-driven scouting assessment.

## Data Source \& Initial Player Selection

The initial player selection was based on rankings published by **Gradient FC**.

Gradient FC's player rankings considered two important dimensions:

- **Player Score:** A performance score derived from the player's statistical metrics.
- **Impact Score:** An assessment of the impact a player produces in matches, beyond simply recording strong individual statistics.

Since the objective was to identify elite midfielders rather than evaluate the entire tournament population, I selected the **top 50 ranked midfielders** from the Gradient FC rankings as the starting dataset.

This provided a focused group of highly ranked players for the subsequent recruitment analysis.

## Midfield Role Classification

Midfielders perform different tactical responsibilities, and evaluating every player against the same criteria would not provide a meaningful recruitment comparison.

To make the analysis practical and easier for a club's recruitment team to interpret, midfield roles were grouped into three broad categories:

| Role | Evaluation Approach |
| --- | --- |
| Attacking Midfielder (AMF) | Greater emphasis on attacking output, positioning and creativity. |
| Box-to-Box Midfielder (B2B) | A balanced evaluation across the different performance categories. |
| Defensive Midfielder (DMF) | Greater emphasis on defensive contributions, alongside passing and progression. |

These three categories form the basis of the role-specific player evaluation and recruitment shortlists.

## Data Collection \& Web Scraping

Python scripts were used to collect player statistics from individual player profile webpages.

The data collection process produced two main CSV files:

- **`world_cup_50_players.csv`** — Contains the selected players, their player names and links to their individual Gradient FC profile webpages.
- **`all_players_metrics.csv`** — Contains the extracted statistical metrics for the selected players. Players are identified by their Gradient FC player numbers rather than their names.

The player numbers in `all_players_metrics.csv` can be matched to individual players using the profile links and player information in `world_cup_50_players.csv`.

The extracted metrics dataset became the primary input for the Python analysis.

## Data Preparation \& Statistical Evaluation

The analysis was performed using Python, Pandas and Jupyter Notebook.

### 1\. Playing-Time Threshold

A minimum playing-time threshold of **300 minutes** was applied to exclude players with insufficient tournament participation.

This threshold was chosen to reduce the influence of highly variable statistics from players with very limited playing time. It represents approximately three full 90-minute matches plus an additional 30 minutes, providing a minimum level of participation for comparison.

### 2\. Metric Direction

The statistical metrics were separated into two groups:

- **Higher is Better:** Metrics where higher values generally indicate stronger performance, such as goals per 90 minutes and shots per 90 minutes.
- **Lower is Better:** Metrics where lower values generally indicate stronger performance, such as positional mistakes and penalties conceded per 90 minutes.

This distinction was used when evaluating and scoring player performance.

### 3\. Eight Performance Categories

The individual statistical metrics were grouped into eight broader performance categories:

1. Goal Threat \& Finishing
2. Attacking Positioning
3. Creativity
4. Passing \& Progression
5. Crossing \& Wide Delivery
6. Ball Carrying \& Dribbling
7. Defensive Contributions
8. Discipline

Each player received a score for every category based on the relevant underlying metrics.

### 4\. Role-Specific Player Scoring

The eight category scores were then used to calculate role-specific player scores.

Different levels of importance were assigned to the performance categories depending on the midfield role being evaluated.

- **AMF Score:** Places greater emphasis on attacking output, positioning and creativity.
- **B2B Score:** Considers performance across the categories in a more balanced manner.
- **DMF Score:** Places greater emphasis on defensive contributions, passing and progression.

This approach allows the same player to be evaluated independently across all three midfield roles rather than being judged using a single overall midfield score.

## Recruitment Shortlisting Methodology

After calculating the role-specific scores, separate selection processes were applied to identify potential recruitment targets.

### Attacking Midfielders (AMF)

Players were evaluated using their AMF scores. A median benchmark was calculated, and players scoring above the median were considered for the recruitment shortlist.

### Box-to-Box Midfielders (B2B)

The same median-based selection approach was applied using the B2B scores. Players scoring above the B2B median were considered for the shortlist.

### Defensive Midfielders (DMF)

A stricter selection process was introduced for defensive midfielders because strong defensive contributions were considered essential for the role.

The selection involved two stages:

1. **Minimum Defensive Threshold:** Players were required to achieve a Defensive Contributions score of at least 50.
2. **Median-Based Selection:** A median DMF score was calculated among the players who passed the defensive threshold. Players scoring above this median were selected for the final DMF recruitment shortlist.

This additional defensive requirement helped prevent players with strong passing or progression scores, but insufficient defensive contributions, from entering the final defensive midfielder shortlist.

## Cost-Efficiency Analysis

Once the role-specific recruitment shortlists were established, the selected players were further evaluated using their estimated market values.

The purpose was to identify players who combined strong role-specific performance with comparatively attractive recruitment costs.

The analysis included:

- Estimated market value comparisons.
- Points per €million.
- Relative cost-efficiency.
- Performance and cost-efficiency classification.

### Recruitment Categories

Players were classified into four recruitment categories:

| Category | Interpretation |
| --- | --- |
| High Performance – High Cost Efficiency | Strong-performing players who also offer attractive cost efficiency. |
| High Performance – Low Cost Efficiency | Strong-performing players with comparatively lower cost efficiency. |
| Low Performance – High Cost Efficiency | More affordable relative to their performance, but with lower performance scores. |
| Low Performance – Low Cost Efficiency | Players who offer neither strong performance nor attractive cost efficiency within the comparison. |

Players in the **High Performance – High Cost Efficiency** category were treated as priority recruitment targets.

The other categories provide additional context for clubs considering alternative recruitment options.

*Market values are estimates and should not be interpreted as confirmed transfer fees.*

## Final Recruitment Datasets

The analysis produced three role-specific recruitment datasets:

- `AMF_Recruitment.csv`
- `B2B_Recruitment.csv`
- `DMF_Recruitment.csv`

Each dataset contains the shortlisted players, their role-specific performance information and recruitment classifications, including priority signing options.

These datasets were exported from the Jupyter Notebook and used as the data sources for the Power BI dashboard.

## Power BI Dashboard

An interactive Power BI dashboard was developed to present the recruitment findings in a format suitable for reviewing and comparing potential targets.

The dashboard includes:

- Executive Overview
- AMF Recruitment Analysis
- AMF Shortlist \& Alternatives
- B2B Recruitment Analysis
- B2B Shortlist \& Alternatives
- DMF Recruitment Analysis
- DMF Shortlist \& Alternatives
- Final Scouting Assessment

The dashboard brings together role-specific performance comparisons, recruitment shortlists, estimated market values and cost-efficiency classifications.

## Repository Structure

``` text
World-Cup-2026-Midfield-Scouting/
│
├── Python/
│   └── World_Cup_2026_Midfield_Analysis.ipynb
│
├── Web_Scraping/
│   └── All files used for web scraping and data extraction
│
├── Data/
│   ├── raw/Final_Recruitment_list
│   │   ├── world_cup_50_players.csv
│   │   └── all_players_metrics.csv
│   │
│   └── processed/
│       ├── AMF_Recruitment.csv
│       ├── B2B_Recruitment.csv
│       └── DMF_Recruitment.csv
│
├── PowerBI/
│   └── World_Cup_2026_Midfield_Scouting_Dashboard.pbix
│
├── README.md
├── requirements.txt
└── .gitignore
```

*The individual HTML files archived during data collection are not listed in this public repository structure. The Web\_Scraping folder contains the files used for scraping and data extraction.*

## Tools \& Technologies

| Tool / Technology | Application |
| --- | --- |
| Python | Data extraction, processing and analysis |
| Pandas | Data cleaning, transformation and statistical evaluation |
| NumPy | Numerical operations |
| BeautifulSoup | HTML parsing and data extraction |
| Requests | Webpage retrieval |
| Jupyter Notebook | Analysis and implementation of the recruitment methodology |
| Power BI | Interactive dashboard and recruitment visualisation |

## Limitations \& Considerations

- The analysis begins with the 50 highest-ranked midfielders selected from Gradient FC's rankings. It is not an evaluation of every midfielder in the tournament.
- The 300-minute threshold excludes players with limited tournament participation.
- The three role categories simplify the variety of tactical responsibilities found in modern midfield positions.
- Statistical performance and role-specific scores cannot independently establish a player's tactical suitability for a particular club.
- Market values are estimates and may differ from actual transfer fees due to contracts, negotiations, player availability and market conditions.
- Further tactical and qualitative scouting is necessary to evaluate consistency, positional awareness, adaptability and suitability within a club's playing system.

## Project Outcome

The project developed a structured recruitment analysis that moves from identifying highly ranked midfielders to evaluating their suitability across different roles and comparing their estimated recruitment value.

It produces three role-specific recruitment shortlists, identifies priority signing options and presents the findings through an interactive Power BI dashboard.

The overall objective is to help a football club distinguish between strong-performing midfielders and those who may offer the most attractive combination of performance, positional suitability and recruitment cost.

## Author

**Albert Charles Palathingal**

B.Tech Computer Science Engineering Graduate

[LinkedIn](<https://www.linkedin.com/in/albert-charles-palathingal-58682a1a5>)