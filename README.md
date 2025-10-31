# WYAS (While You Are Sleeping) — Global Economy Trends Morning Update

## Summary
**WYAS** automatically collects recent Google Trends topics, summarizes them into an HTML table, and sends you a **daily morning email update**.  

It’s designed to run on a schedule (e.g., 7 AM daily) and can be customized for different countries or time zones.

---

## Project Layout
| Path | Description |
|------|--------------|
| `scripts/main.py` | Main entry point — runs the full pipeline |
| `scripts/read_trends.py` | Scraping and data collection logic |
| `scripts/send_email.py` | Builds HTML content and sends email |
| `scripts/config.py` | Contains scheduling constants (`SCHEDULED_HR`, `SCHEDULED_MIN`, `TIME_ZONE`) |
| `requirements.txt` | Project dependencies |
| `data/` | Runtime data files (`trends_table.csv`, `timestamp.txt`, etc.) |
| `.gitignore` | Excludes local data files and other sensitive info |

---

## Requirements
- **Python 3.9+** recommended  
- See `requirements.txt`
