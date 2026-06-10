import plotly.graph_objects as go

# Skills data from your profile
skills = ["Excel (VBA)", "Accounting", "Python", "Taxation", "Financial Modeling"]
scores = [100, 100, 100, 100, 100]

fig = go.Figure(go.Bar(
    x=scores, y=skills, orientation='h',
    marker=dict(color='rgba(0, 78, 146, 0.8)')
))

fig.update_layout(
    title="Technical Proficiency (%)",
    xaxis=dict(range=[0, 100]),
    yaxis=dict(autorange="reversed"),
    height=350, margin=dict(l=20, r=20, t=40, b=20),
    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
)

# Save the chart as an HTML snippet
fig.write_html("skills_chart.html", full_html=False, include_plotlyjs='cdn')
print("Success: skills_chart.html has been created!")