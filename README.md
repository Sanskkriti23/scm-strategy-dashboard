# SCM Strategy Dashboard - Streamlit App

An interactive dashboard for analyzing supply chain ERP strategy, competitive landscape, and go-to-market planning.

## Features

- **Overview**: Strategic insights and priority analysis
- **Competitors**: Competitive landscape with AI capability analysis
- **Opportunities**: AI feature differentiation matrix
- **Segments**: Target market analysis for Bangalore beachhead
- **Revenue**: Multi-stream revenue model breakdown
- **Growth**: Market projections and 90-day pilot playbook

## Quick Start - Local Testing

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run scm_dashboard_app.py
```

3. Open your browser to `http://localhost:8501`

## Deploy to Streamlit Cloud (Free!)

### Option 1: Deploy via Streamlit Cloud Website

1. **Create a GitHub account** (if you don't have one) at https://github.com

2. **Create a new repository:**
   - Go to https://github.com/new
   - Name it something like `scm-strategy-dashboard`
   - Make it Public
   - Click "Create repository"

3. **Upload your files to GitHub:**
   - Click "uploading an existing file"
   - Drag and drop these files:
     - `scm_dashboard_app.py`
     - `requirements.txt`
     - `README.md` (this file)
   - Click "Commit changes"

4. **Deploy on Streamlit Cloud:**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Sign in with GitHub
   - Select your repository: `scm-strategy-dashboard`
   - Main file path: `scm_dashboard_app.py`
   - Click "Deploy!"

5. **Share your app:**
   - You'll get a URL like: `https://yourname-scm-strategy-dashboard.streamlit.app`
   - Share this URL with anyone!

### Option 2: Deploy via GitHub CLI (for developers)

```bash
# Initialize git repo
git init
git add .
git commit -m "Initial commit"

# Create GitHub repo and push
gh repo create scm-strategy-dashboard --public --source=. --push

# Then follow steps 4-5 above
```

## Using the Dashboard

### Navigation
- Use the **sidebar** to switch between different views
- Each tab provides interactive charts and detailed analysis

### Key Insights

**Overview Tab:**
- See all 10 strategic insights at a glance
- View top priority opportunities ranked by impact × ease
- Analyze revenue stream scores

**Competitors Tab:**
- Compare AI capabilities vs SME accessibility
- Identify market opportunities based on competitor gaps
- View detailed scoring across all dimensions

**Opportunities Tab:**
- Radar chart showing SME differentiation potential
- Implementation complexity vs ROI analysis
- Priority matrix for market gaps

**Segments Tab:**
- Bangalore-focused target segments
- Pain points and conversion metrics
- Strategic rationale for beachhead market

**Revenue Tab:**
- 7 revenue stream models analyzed
- Recurring vs one-time revenue mix
- Scalability and margin breakdown

**Growth Tab:**
- Market projections through 2030
- 90-day pilot playbook timeline
- Sales motion phases and target companies

## Customization

To customize the data:

1. Edit the `load_data()` function in `scm_dashboard_app.py`
2. Update the DataFrames with your own data
3. Save and the app will automatically reload

## Sharing with Your Team

Once deployed on Streamlit Cloud:
- ✅ No installation needed for viewers
- ✅ Works on any device (desktop, tablet, mobile)
- ✅ Always shows latest version
- ✅ Free hosting with reasonable usage limits

## Troubleshooting

**App won't start?**
- Check that all dependencies are in `requirements.txt`
- Ensure Python version compatibility (3.8+)

**Charts not displaying?**
- Check browser console for errors
- Try a different browser (Chrome/Firefox recommended)

**Need to update the app?**
- Just push changes to GitHub
- Streamlit Cloud auto-deploys within minutes

## Support

For issues or questions:
- Check Streamlit docs: https://docs.streamlit.io
- Community forum: https://discuss.streamlit.io

---

Built with Streamlit 🎈
