# 📊 Auto Video Upload Optimizer

A data science web app that analyzes video upload performance and recommends the best posting time based on data. Created to help content creators use data to optimize their posting schedules and maximize reach.

## 🚀 Features
- Upload CSV of video analytics data
- Analyze best performing day
- Analyze best performing upload time
- Heatmap visualization of performance patterns
- Automatic recommendation of optimal upload time

## 🛠 Tech Stack
- Python
- Streamlit
- Pandas
- Seaborn
- Matplotlib

## 🌐 Live Demo
https://video-upload-optimizer-ykmbbpnjetaaxdjylklr7n.streamlit.app/

## 🚀 How to Use

1. Open the web app:
   https://video-upload-optimizer-ykmbbpnjetaaxdjylklr7n.streamlit.app/

2. Prepare a CSV file containing your video performance data.

3. Make sure the CSV follows the required format shown below.

4. Upload the CSV file to the app.

5. Review the results:
   - Best performing day
   - Best performing upload time
   - Performance heatmap
   - Recommended upload schedule

## 📊 Data Format

Upload a CSV file with the following columns (Example):

| Date | Day | Time Posted | Views Day 3 |
|------|-----|-------------|-------------|
| 2025-01-27 | Tuesday | PM07:00 | 559 |
| 2025-02-02 | Tuesday | PM12:00 | 1980 |

### Column Description:
- **Date** → upload date of the video
- **Day** → weekday name (Monday–Sunday)
- **Time Posted** → format like `PM07:00` or `AM10:00`
- **Views Day 3** → number of views after 3 days

## ⚡ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
