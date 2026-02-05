import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="SCM Strategy Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 0.5rem;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .insight-card {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        border-left: 4px solid;
    }
    .critical { background-color: #fef2f2; border-color: #ef4444; }
    .warning { background-color: #fffbeb; border-color: #f59e0b; }
    .strength { background-color: #f0fdf4; border-color: #10b981; }
    .opportunity { background-color: #eff6ff; border-color: #3b82f6; }
</style>
""", unsafe_allow_html=True)

# Data
@st.cache_data
def load_data():
    # Competitor data
    competitors = pd.DataFrame([
        {'vendor': 'Kinaxis', 'segment': 'Large Enterprise', 'coverage': 9, 'ai': 9, 'cost': 2, 'smeAccess': 1, 'opportunity': 8},
        {'vendor': 'SAP B1/SCM', 'segment': 'Mid + Large', 'coverage': 10, 'ai': 9, 'cost': 2, 'smeAccess': 3, 'opportunity': 7},
        {'vendor': 'Infor GT Nexus', 'segment': 'Enterprise', 'coverage': 8, 'ai': 7, 'cost': 3, 'smeAccess': 2, 'opportunity': 8},
        {'vendor': 'Manhattan', 'segment': 'Enterprise Retail', 'coverage': 8, 'ai': 8, 'cost': 2, 'smeAccess': 2, 'opportunity': 7},
        {'vendor': 'Blue Yonder', 'segment': 'Enterprise', 'coverage': 9, 'ai': 9, 'cost': 2, 'smeAccess': 1, 'opportunity': 8},
        {'vendor': 'o9 Solutions', 'segment': 'Enterprise', 'coverage': 8, 'ai': 9, 'cost': 2, 'smeAccess': 1, 'opportunity': 9},
        {'vendor': 'FourKites', 'segment': 'Enterprise', 'coverage': 6, 'ai': 7, 'cost': 5, 'smeAccess': 4, 'opportunity': 6},
        {'vendor': 'Project44', 'segment': 'Enterprise', 'coverage': 6, 'ai': 7, 'cost': 5, 'smeAccess': 4, 'opportunity': 6},
        {'vendor': 'Bizongo', 'segment': 'India SME/Mid', 'coverage': 5, 'ai': 5, 'cost': 7, 'smeAccess': 8, 'opportunity': 5}
    ])
    
    # Market gaps
    market_gaps = pd.DataFrame([
        {'gap': 'SME fragmentation', 'priority': 'Critical', 'impact': 9, 'ease': 8, 'value': 'Removes tool sprawl'},
        {'gap': 'Enterprise complexity', 'priority': 'High', 'impact': 8, 'ease': 7, 'value': 'Faster adoption'},
        {'gap': 'Weak India localization', 'priority': 'Critical', 'impact': 10, 'ease': 9, 'value': 'Regulatory fit'},
        {'gap': 'Excel planning', 'priority': 'High', 'impact': 8, 'ease': 8, 'value': 'Better decisions'},
        {'gap': 'Manual vendor mgmt', 'priority': 'Medium', 'impact': 7, 'ease': 7, 'value': 'Performance visibility'},
        {'gap': 'No cross-module sync', 'priority': 'High', 'impact': 8, 'ease': 6, 'value': 'Dept alignment'},
        {'gap': 'Static dashboards', 'priority': 'Medium', 'impact': 7, 'ease': 8, 'value': 'Real-time ops view'},
        {'gap': 'High license cost', 'priority': 'Critical', 'impact': 9, 'ease': 9, 'value': 'Lower entry barrier'},
        {'gap': 'No SME AI', 'priority': 'Critical', 'impact': 10, 'ease': 7, 'value': 'Decision intelligence'}
    ])
    market_gaps['score'] = (market_gaps['impact'] * 0.6 + market_gaps['ease'] * 0.4).round(1)
    
    # AI Features
    ai_features = pd.DataFrame([
        {'feature': 'Inventory AI Copilot', 'smeDiff': 9, 'enterpriseHas': 3, 'implementation': 7, 'roi': 9},
        {'feature': 'Demand Forecast AI', 'smeDiff': 7, 'enterpriseHas': 8, 'implementation': 8, 'roi': 8},
        {'feature': 'AI Reorder Engine', 'smeDiff': 8, 'enterpriseHas': 5, 'implementation': 7, 'roi': 9},
        {'feature': 'Supplier AI Scoring', 'smeDiff': 8, 'enterpriseHas': 4, 'implementation': 6, 'roi': 7},
        {'feature': 'Conversational Copilot', 'smeDiff': 9, 'enterpriseHas': 2, 'implementation': 6, 'roi': 8},
        {'feature': 'Anomaly Detection', 'smeDiff': 7, 'enterpriseHas': 6, 'implementation': 8, 'roi': 8},
        {'feature': 'Scenario Simulation', 'smeDiff': 8, 'enterpriseHas': 7, 'implementation': 5, 'roi': 7},
        {'feature': 'Document AI', 'smeDiff': 9, 'enterpriseHas': 4, 'implementation': 9, 'roi': 10},
        {'feature': 'Redistribution AI', 'smeDiff': 9, 'enterpriseHas': 3, 'implementation': 6, 'roi': 8}
    ])
    
    # Target segments
    target_segments = pd.DataFrame([
        {
            'name': 'Industrial SMEs (Peenya)',
            'priority': 10,
            'marketSize': 850,
            'avgDeal': 15000,
            'conversionRate': 35,
            'painPoints': 'Stockouts/overstock, Manual PO/GRN, Invoice mismatches',
            'modules': 'Inventory, PO/GRN, WMS-lite, Transport, Document AI'
        },
        {
            'name': 'Distributors/Wholesalers',
            'priority': 9,
            'marketSize': 620,
            'avgDeal': 18000,
            'conversionRate': 30,
            'painPoints': 'Order-to-cash gaps, Delivery failures, Excel planning',
            'modules': 'Order Mgmt, Inventory, Route/Dispatch, Control Tower, CRM'
        },
        {
            'name': 'D2C/E-commerce',
            'priority': 8,
            'marketSize': 480,
            'avgDeal': 12000,
            'conversionRate': 40,
            'painPoints': 'Forecasting, Inventory sync, Shipment SLA tracking',
            'modules': 'Inventory, Sales channels, Forecasting, Control Tower'
        },
        {
            'name': '3PLs/Transport',
            'priority': 7,
            'marketSize': 340,
            'avgDeal': 20000,
            'conversionRate': 25,
            'painPoints': 'Shipment tracking, Delay prediction, Billing disputes',
            'modules': 'Transport, Tracking, Control Tower, Invoice/Claims'
        }
    ])
    
    # Revenue streams
    revenue_streams = pd.DataFrame([
        {'stream': 'Core subscription', 'segment': 'SME + Mid', 'recurring': 100, 'margin': 85, 'scalability': 9},
        {'stream': 'Seat-based', 'segment': 'Mid-market teams', 'recurring': 100, 'margin': 88, 'scalability': 8},
        {'stream': 'Usage-based AI', 'segment': 'SMEs wanting ROI', 'recurring': 80, 'margin': 75, 'scalability': 10},
        {'stream': 'Transaction-based logistics', 'segment': 'Distributors + fleets', 'recurring': 70, 'margin': 65, 'scalability': 9},
        {'stream': 'Implementation', 'segment': 'Mid-market', 'recurring': 0, 'margin': 40, 'scalability': 5},
        {'stream': 'Integration marketplace', 'segment': 'All', 'recurring': 90, 'margin': 95, 'scalability': 10},
        {'stream': 'Premium support/SLA', 'segment': 'Mid-market', 'recurring': 100, 'margin': 90, 'scalability': 7}
    ])
    revenue_streams['score'] = (revenue_streams['recurring'] * 0.3 + revenue_streams['margin'] * 0.3 + revenue_streams['scalability'] * 10 * 0.4).round(1)
    
    # Market growth
    market_growth = pd.DataFrame([
        {'year': 2024, 'logistics': 215, 'warehouse': 8.2, 'wms': 1.4},
        {'year': 2025, 'logistics': 245, 'warehouse': 9.1, 'wms': 1.6},
        {'year': 2026, 'logistics': 280, 'warehouse': 10.2, 'wms': 1.9},
        {'year': 2027, 'logistics': 320, 'warehouse': 11.5, 'wms': 2.2},
        {'year': 2028, 'logistics': 365, 'warehouse': 13.0, 'wms': 2.6},
        {'year': 2029, 'logistics': 415, 'warehouse': 14.8, 'wms': 3.1},
        {'year': 2030, 'logistics': 475, 'warehouse': 16.9, 'wms': 3.7}
    ])
    
    # Strategic insights
    strategic_insights = [
        {'category': 'Positioning', 'insight': 'Stay SME-first and avoid enterprise feature overload', 'status': 'critical', 'impact': 'high'},
        {'category': 'Moat', 'insight': 'Embedded AI + Workflow + Localization combined', 'status': 'strength', 'impact': 'high'},
        {'category': 'Wedge Market', 'insight': 'India compliance + GST + e-invoice integration', 'status': 'opportunity', 'impact': 'high'},
        {'category': 'Narrative', 'insight': 'Control Tower + Copilot fusion central in pitch', 'status': 'strength', 'impact': 'medium'},
        {'category': 'Competition', 'insight': 'Compete on speed + usability + cost, NOT features', 'status': 'critical', 'impact': 'high'},
        {'category': 'Pricing', 'insight': 'Modular pricing aligns with SME buying behavior', 'status': 'strength', 'impact': 'high'},
        {'category': 'Quick Win', 'insight': 'Document AI + auto data ingestion high ROI', 'status': 'opportunity', 'impact': 'high'},
        {'category': 'Differentiator', 'insight': 'Conversational SCM layer strong demo tool', 'status': 'strength', 'impact': 'medium'},
        {'category': 'Risk', 'insight': 'Scope creep - ship core execution first, AI second', 'status': 'warning', 'impact': 'high'},
        {'category': 'GTM', 'insight': 'Target multi-warehouse SMEs and distributors first', 'status': 'opportunity', 'impact': 'high'}
    ]
    
    return competitors, market_gaps, ai_features, target_segments, revenue_streams, market_growth, strategic_insights

competitors, market_gaps, ai_features, target_segments, revenue_streams, market_growth, strategic_insights = load_data()

# Header
st.markdown('<div class="main-header">📊 SCM Strategy Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Interactive analysis of supply chain ERP strategy, market positioning, and GTM roadmap</div>', unsafe_allow_html=True)

# Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Market Size (2027)",
        value="₹320B",
        delta="↑ 48% growth"
    )

with col2:
    st.metric(
        label="Target Companies",
        value="2,290",
        delta="Bangalore region"
    )

with col3:
    st.metric(
        label="Avg Deal Size",
        value="₹15-20K",
        delta="Monthly recurring"
    )

with col4:
    st.metric(
        label="AI Features",
        value="9",
        delta="Differentiators"
    )

st.markdown("---")

# Sidebar
st.sidebar.title("🎯 Navigation")
tab_selection = st.sidebar.radio(
    "Select View:",
    ["Overview", "Competitors", "Opportunities", "Segments", "Revenue", "Growth"]
)

# Export button
if st.sidebar.button("📥 Export Data"):
    st.sidebar.success("Export functionality would download all data as CSV/Excel")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Data Sources")
st.sidebar.markdown("- IBEF Case Studies")
st.sidebar.markdown("- Mordor Intelligence")
st.sidebar.markdown("- Grand View Research")

# Tab content
if tab_selection == "Overview":
    st.header("🎯 Strategic Insights")
    
    # Display insights in grid
    cols = st.columns(2)
    for idx, item in enumerate(strategic_insights):
        with cols[idx % 2]:
            status_class = item['status']
            impact_badge = "⭐ High Impact" if item['impact'] == 'high' else ""
            
            st.markdown(f"""
            <div class="insight-card {status_class}">
                <strong>{item['category']}</strong> {impact_badge}<br/>
                <span style="font-size: 0.9rem;">{item['insight']}</span>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Two columns for priority opportunities and revenue analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Top Priority Opportunities")
        top_gaps = market_gaps.nlargest(5, 'score')
        for _, gap in top_gaps.iterrows():
            priority_color = "🔴" if gap['priority'] == 'Critical' else "🟠" if gap['priority'] == 'High' else "🟡"
            st.markdown(f"""
            **{gap['gap']}** {priority_color}  
            Score: **{gap['score']}** | Impact: {gap['impact']}/10 | Ease: {gap['ease']}/10  
            _{gap['value']}_
            """)
            st.markdown("---")
    
    with col2:
        st.subheader("💰 Revenue Stream Analysis")
        top_revenue = revenue_streams.nlargest(5, 'score')
        for _, stream in top_revenue.iterrows():
            st.markdown(f"""
            **{stream['stream']}**  
            Score: **{stream['score']}** | Recurring: {stream['recurring']}% | Margin: {stream['margin']}% | Scale: {stream['scalability']}/10  
            _Target: {stream['segment']}_
            """)
            st.markdown("---")

elif tab_selection == "Competitors":
    st.header("🏆 Competitive Landscape Analysis")
    st.markdown("Positioning analysis showing where competitors are strong and where opportunities exist for SME-focused solutions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("AI Capability vs SME Accessibility")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=competitors['vendor'],
            y=competitors['ai'],
            name='AI Strength',
            marker_color='#3b82f6'
        ))
        fig.add_trace(go.Bar(
            x=competitors['vendor'],
            y=competitors['smeAccess'],
            name='SME Access',
            marker_color='#10b981'
        ))
        fig.update_layout(
            barmode='group',
            xaxis_tickangle=-45,
            height=400,
            xaxis_title="",
            yaxis_title="Score (0-10)"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Market Opportunity Score")
        sorted_comp = competitors.sort_values('opportunity', ascending=True)
        fig = go.Figure(go.Bar(
            x=sorted_comp['opportunity'],
            y=sorted_comp['vendor'],
            orientation='h',
            marker_color='#f59e0b'
        ))
        fig.update_layout(
            height=400,
            xaxis_title="Opportunity Score",
            yaxis_title=""
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📊 Detailed Competitor Comparison")
    
    # Create styled dataframe
    display_df = competitors[['vendor', 'segment', 'coverage', 'ai', 'cost', 'smeAccess', 'opportunity']].copy()
    display_df.columns = ['Vendor', 'Segment', 'Coverage', 'AI', 'Cost', 'SME Access', 'Opportunity']
    
    st.dataframe(
        display_df.style.background_gradient(cmap='RdYlGn', subset=['Coverage', 'AI', 'SME Access', 'Opportunity'])
                        .background_gradient(cmap='RdYlGn', subset=['Cost']),
        use_container_width=True
    )

elif tab_selection == "Opportunities":
    st.header("💡 AI Feature Differentiation Matrix")
    st.markdown("Analysis of AI features showing SME differentiation potential vs enterprise adoption and implementation complexity")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Feature Differentiation Radar")
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=ai_features['smeDiff'].tolist(),
            theta=ai_features['feature'].tolist(),
            fill='toself',
            name='SME Diff',
            line_color='#3b82f6'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=ai_features['enterpriseHas'].tolist(),
            theta=ai_features['feature'].tolist(),
            fill='toself',
            name='Enterprise Has',
            line_color='#ef4444',
            opacity=0.5
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=True,
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Implementation vs ROI")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=ai_features['feature'],
            y=ai_features['implementation'],
            name='Implementation Ease',
            marker_color='#f59e0b'
        ))
        fig.add_trace(go.Bar(
            x=ai_features['feature'],
            y=ai_features['roi'],
            name='ROI Potential',
            marker_color='#10b981'
        ))
        fig.update_layout(
            barmode='group',
            xaxis_tickangle=-45,
            height=400,
            xaxis_title="",
            yaxis_title="Score (0-10)"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🎯 Priority Matrix: Impact vs Implementation Ease")
    
    cols = st.columns(2)
    for idx, (_, gap) in enumerate(market_gaps.nlargest(9, 'score').iterrows()):
        with cols[idx % 2]:
            priority_emoji = "🔴" if gap['priority'] == 'Critical' else "🟠" if gap['priority'] == 'High' else "🟡"
            st.markdown(f"""
            **{gap['gap']}** {priority_emoji}  
            Priority Score: **{gap['score']}**  
            Impact: {gap['impact']}/10 | Ease: {gap['ease']}/10  
            💡 {gap['value']}
            """)

elif tab_selection == "Segments":
    st.header("🎯 Target Segment Analysis")
    st.markdown("Bangalore-focused GTM strategy with prioritized segments based on pain points, market size, and conversion potential")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Segment Priority & Market Size")
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig.add_trace(
            go.Bar(x=target_segments['name'], y=target_segments['priority'], name="Priority Score", marker_color='#3b82f6'),
            secondary_y=False
        )
        
        fig.add_trace(
            go.Bar(x=target_segments['name'], y=target_segments['marketSize'], name="Market Size (M)", marker_color='#10b981'),
            secondary_y=True
        )
        
        fig.update_xaxes(tickangle=-45)
        fig.update_yaxes(title_text="Priority Score", secondary_y=False)
        fig.update_yaxes(title_text="Market Size (₹M)", secondary_y=True)
        fig.update_layout(height=400)
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Deal Size vs Conversion Rate")
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig.add_trace(
            go.Bar(x=target_segments['name'], y=target_segments['avgDeal'], name="Avg Deal (₹K)", marker_color='#8b5cf6'),
            secondary_y=False
        )
        
        fig.add_trace(
            go.Bar(x=target_segments['name'], y=target_segments['conversionRate'], name="Conversion %", marker_color='#14b8a6'),
            secondary_y=True
        )
        
        fig.update_xaxes(tickangle=-45)
        fig.update_yaxes(title_text="Deal Size (₹K)", secondary_y=False)
        fig.update_yaxes(title_text="Conversion %", secondary_y=True)
        fig.update_layout(height=400)
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📋 Detailed Segment Breakdown")
    
    for _, segment in target_segments.iterrows():
        with st.expander(f"**{segment['name']}** - Priority: {segment['priority']}/10"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Market Size", f"₹{segment['marketSize']}M")
            with col2:
                st.metric("Avg Deal", f"₹{segment['avgDeal']:,}")
            with col3:
                st.metric("Conversion Rate", f"{segment['conversionRate']}%")
            
            st.markdown(f"**Pain Points:** {segment['painPoints']}")
            st.markdown(f"**Lead Modules:** {segment['modules']}")
    
    st.markdown("---")
    st.info("""
    **🌏 Why Bangalore is Strategic:**
    - Dense SMB industrial clusters (Peenya area) with thousands of manufacturers
    - Strong SaaS adoption culture and tech-savvy businesses
    - Access to implementation partners and technical support ecosystem
    - Clustered industries enable template-driven deployments and faster iteration
    """)

elif tab_selection == "Revenue":
    st.header("💰 Revenue Model Analysis")
    st.markdown("Multi-stream revenue architecture designed for SME buying behavior with low friction entry and modular expansion")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue Stream Comparison")
        sorted_rev = revenue_streams.sort_values('score', ascending=False)
        fig = go.Figure(go.Bar(
            x=sorted_rev['stream'],
            y=sorted_rev['score'],
            marker_color=['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899', '#14b8a6', '#6366f1'],
            text=sorted_rev['score'],
            textposition='outside'
        ))
        fig.update_layout(
            xaxis_tickangle=-45,
            height=400,
            xaxis_title="",
            yaxis_title="Overall Score"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Recurring vs One-time Revenue")
        fig = go.Figure(data=[go.Pie(
            labels=['Recurring (Core + Seats)', 'Usage-based (AI + Logistics)', 'Ecosystem (Integrations + Support)', 'One-time (Implementation)'],
            values=[40, 35, 20, 5],
            marker_colors=['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6'],
            textinfo='label+percent'
        )])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📊 Detailed Revenue Stream Breakdown")
    
    for _, stream in revenue_streams.iterrows():
        with st.expander(f"**{stream['stream']}** - Score: {stream['score']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Recurring Revenue", f"{stream['recurring']}%")
            with col2:
                st.metric("Margin", f"{stream['margin']}%")
            with col3:
                st.metric("Scalability", f"{stream['scalability']}/10")
            
            st.markdown(f"**Target Segment:** {stream['segment']}")
            
            # Progress bars
            st.progress(stream['recurring'] / 100)
    
    st.markdown("---")
    st.success("""
    **✅ Revenue Model Strategy:**
    - **Low Friction Entry:** Module-based pricing lets SMEs start small
    - **Usage-based AI:** Pay-per-use reduces upfront cost and aligns with value
    - **Ecosystem Lock-in:** Integration marketplace drives long-term stickiness
    """)

elif tab_selection == "Growth":
    st.header("📈 Market Growth Projections")
    st.markdown("India logistics, warehouse, and WMS market forecasts through 2030 showing strong tailwinds for SCM solutions")
    
    st.subheader("Market Size Growth (₹ Billions)")
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=market_growth['year'],
        y=market_growth['logistics'],
        mode='lines+markers',
        name='Logistics Market',
        line=dict(color='#3b82f6', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=market_growth['year'],
        y=market_growth['warehouse'],
        mode='lines+markers',
        name='Warehouse Market',
        line=dict(color='#10b981', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=market_growth['year'],
        y=market_growth['wms'],
        mode='lines+markers',
        name='WMS Market',
        line=dict(color='#8b5cf6', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        height=450,
        xaxis_title="Year",
        yaxis_title="Market Size (₹B)",
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Logistics Market (2030)",
            value="₹475B",
            delta="+121% (2024-2030)",
            delta_color="normal"
        )
        st.caption("CAGR: ~14.2% annually")
    
    with col2:
        st.metric(
            label="Warehouse Market (2030)",
            value="₹16.9B",
            delta="+106% (2024-2030)",
            delta_color="normal"
        )
        st.caption("CAGR: ~12.8% annually")
    
    with col3:
        st.metric(
            label="WMS Market (2030)",
            value="₹3.7B",
            delta="+164% (2024-2030)",
            delta_color="normal"
        )
        st.caption("CAGR: ~17.5% annually")
    
    st.markdown("---")
    
    st.subheader("🚀 90-Day Pilot Playbook")
    
    phases = [
        {"week": "Week 1-2", "title": "Baseline Mapping", "desc": "Current tools assessment, SKU count, warehouse locations, order volume analysis", "color": "#3b82f6"},
        {"week": "Week 3-4", "title": "Core Module Go-Live", "desc": "Inventory + PO/GRN live, document AI ingestion, minimum integrations", "color": "#10b981"},
        {"week": "Week 5-8", "title": "Execution Layer", "desc": "Order + dispatch tracking, control tower activation, alerting setup", "color": "#8b5cf6"},
        {"week": "Week 9-12", "title": "Intelligence Layer", "desc": "Forecasting + reorder suggestions, KPI review, case study documentation", "color": "#f59e0b"}
    ]
    
    for phase in phases:
        st.markdown(f"""
        <div style="background-color: {phase['color']}22; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid {phase['color']}; margin-bottom: 1rem;">
            <strong style="color: {phase['color']};">{phase['week']}</strong><br/>
            <strong>{phase['title']}</strong><br/>
            <span style="font-size: 0.9rem;">{phase['desc']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📍 Sales Motion Phases")
        st.markdown("""
        **Phase 1 (0-6 months)**  
        Founder-led sales + 5-10 design partners, weekly on-site mapping, fast templates
        
        **Phase 2 (6-18 months)**  
        Inside sales + channel partners (accounting firms, logistics aggregators, ERP implementers)
        
        **Phase 3 (18+ months)**  
        Platform ecosystem (3PL connectors, GST/e-invoice integrations, marketplace add-ons)
        """)
    
    with col2:
        st.subheader("🎯 Target Companies (Examples)")
        companies = [
            ("Max Milan Tooling (Peenya)", "Industrial tooling, SKU/vendor complexity"),
            ("Axis Electric Corporation (Peenya)", "Component supply, frequent PO cycles"),
            ("Udaan (Bengaluru HQ)", "B2B trade platform, integration benchmark"),
            ("MTR Foods (Bengaluru)", "Complex supply chain, enterprise reference")
        ]
        for company, desc in companies:
            st.markdown(f"**{company}**  \n_{desc}_")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; font-size: 0.9rem;">
    <p>Supply Chain ERP Strategy Dashboard • Data sources: IBEF, Mordor Intelligence, Grand View Research</p>
    <p>Interactive analysis tool for market validation and GTM planning</p>
</div>
""", unsafe_allow_html=True)
