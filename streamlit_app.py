import math
import streamlit as st

"""
# Calculate Sled's ROI 

This tool will help you determine the ROI of **[Sled](https://www.sled.so/) 🛷** for your organization.

---
"""

"""
## Value Drivers

These are the value drivers for Sled.  Please enter the values for your organization.  
All results are in USD / year.
"""

cola, colb = st.columns(2)

with cola:
    num_people = st.slider("Number of data professionals (engineers, analysts, leaders)", 1, 100, 15)
    retention = st.slider("Avg. retention time in years", 1.0, 5.0, 2.0)
    salary = st.slider("Cost of labour for 1 full-time employee", 40000, 200000, 80000)

    """
    #### Higher Productivity
    """

    productivity_value = round(num_people * salary * 0.15)
    onboarding_value = round(num_people * salary * 1/retention * 1/12)

    st.metric('More effective data team', "{:,}$".format(productivity_value + onboarding_value), delta=None, delta_color="normal", help='On average data professionals save 6 hours / week (15%) because of faster troubleshooting, better change impact analysis and less duplicate and manual work. New data professionals save at least 1 month of onboarding time.')


with colb:
    options = [5 * 2 ** i for i in range(0, 10)]
    revenue = st.select_slider("Revenue of your company in million USD", options=options, value=options[3]) * 1e6
    perc_decision_m = st.slider("% of decision makers working on Snowflake data", 0.0, 1.0, 0.2)
    num_dq_incidents = st.slider(" days per month with data quality incidents", 1, 30, 7)

    """
    #### Cost of Bad Data
    """
    bad_data_cost = round(revenue * perc_decision_m * num_dq_incidents / 30 * 0.15)
    st.metric('Business opportunity cost', "{:,}$".format(bad_data_cost), delta=None, delta_color="normal", help='The business opportunity cost is the revenue that is lost because of bad data. Decision based on bad data are typically 15% less effective, e.g. inefficiently allocated marketing budget.')


"""
---

## Investment
"""
# generate array of option starting from 2000 and increasing exponentially
# by 2.0 until it reaches 500000
options = [2000 * 2 ** i for i in range(0, 10)]
total_points = st.select_slider("Number of analytics assets (Snowflake tables, columns, BI dashboards, ...)", options=options, value=options[3])
price_year = round(math.sqrt(total_points) * 10) * 12
st.metric('Sled\'s price per year', "{:,}$".format(price_year), delta=None, delta_color="normal", help=None)

"""

---
## Return on Investment
"""
multiple = (onboarding_value + productivity_value + bad_data_cost) /(price_year)
st.metric('ROI over lifetime', f"{round(multiple * 100)}%", delta=None, delta_color="normal", help=f"Value Drivers / Investment")
st.write(f" {round(multiple)}x your investment in Sled with a more productive data team, trustworthy data for your organization and therefore better business decisions. 🌲")
