import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Royal Enfield Configurator & Booking",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Custom CSS Styling
st.markdown(
    """
    <style>
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #1e1e1e;
    }
    ::-webkit-scrollbar-thumb {
        background: #d32f2f;
        border-radius: 4px;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #e50914;
        margin-bottom: 0px;
        letter-spacing: 1px;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #a0a0a0;
        margin-bottom: 25px;
    }
    .price-tag {
        font-size: 2rem;
        font-weight: 700;
        color: #2e7d32;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Complete Bikes Dataset
bikes = {
    "Bullet 350": {
        "tagline": "1932: Made Like A Gun",
        "variants": ["Base / Military", "Standard", "Black Gold"],
        "paints": [
            "Military Red",
            "Military Black",
            "Standard Black",
            "Standard Maroon",
            "Black Gold",
        ],
        "base_price": 173500,
        "specs": {
            "Engine": "349cc Single Cylinder, Air-Oil Cooled (J-Series)",
            "Power": "20.2 BHP @ 6100 RPM",
            "Torque": "27 Nm @ 4000 RPM",
            "Transmission": "5-Speed Constant Mesh",
            "Fuel Capacity": "13 Litres",
            "Brakes": "Front Disc / Rear Drum (Dual ABS optional)",
        },
    },
    "Classic 350": {
        "tagline": "Be Reborn",
        "variants": ["Heritage", "Signals", "Dark", "Chrome"],
        "paints": [
            "Stealth Black",
            "Gunmetal Grey",
            "Forest Green",
            "Halcyon Black",
            "Chrome Red",
        ],
        "base_price": 193000,
        "specs": {
            "Engine": "349cc Single Cylinder, Air-Oil Cooled",
            "Power": "20.2 BHP @ 6100 RPM",
            "Torque": "27 Nm @ 4000 RPM",
            "Transmission": "5-Speed",
            "Fuel Capacity": "13 Litres",
            "Brakes": "Dual Channel ABS",
        },
    },
    "Hunter 350": {
        "tagline": "Shot of Motorcycling",
        "variants": ["Factory Series", "Metro Dapper", "Metro Rebel"],
        "paints": [
            "Dapper Ash",
            "Rebel Black",
            "Factory Silver",
            "Rebel Blue",
            "Tokyo Black",
        ],
        "base_price": 149900,
        "specs": {
            "Engine": "349cc Single Cylinder, Air-Oil Cooled",
            "Power": "20.2 BHP @ 6100 RPM",
            "Torque": "27 Nm @ 4000 RPM",
            "Transmission": "5-Speed",
            "Fuel Capacity": "13 Litres",
            "Brakes": "Single / Dual ABS Options",
        },
    },
    "Himalayan 450": {
        "tagline": "Built for All Roads. Built for No Roads.",
        "variants": ["Base", "Pass", "Summit"],
        "paints": ["Kaza Brown", "Slate Poppy Blue", "Hanle Black", "Kamet White"],
        "base_price": 285000,
        "specs": {
            "Engine": "452cc Sherpa Liquid-Cooled Engine",
            "Power": "40 BHP @ 8000 RPM",
            "Torque": "40 Nm @ 5500 RPM",
            "Transmission": "6-Speed with Slip & Assist",
            "Fuel Capacity": "17 Litres",
            "Brakes": "Dual Channel Switchable ABS",
        },
    },
    "Interceptor 650": {
        "tagline": "Easy Got Back",
        "variants": ["Standard", "Custom", "Special Alloy"],
        "paints": [
            "Canyon Red",
            "Sunset Strip",
            "Baker Express",
            "Mark 2 Chrome",
            "Barcelona Blue",
        ],
        "base_price": 303000,
        "specs": {
            "Engine": "648cc Parallel Twin, 4-stroke",
            "Power": "47 BHP @ 7150 RPM",
            "Torque": "52 Nm @ 5250 RPM",
            "Transmission": "6-Speed",
            "Fuel Capacity": "13.7 Litres",
            "Brakes": "ByBre Dual Channel ABS",
        },
    },
}

# 4. Accessories Catalog
accessories_catalog = {
    "Touring Mirrors": 6500,
    "Sump Guard / Engine Protector": 3200,
    "Engine Guard (Leg Guard)": 4500,
    "Touring Seat": 4800,
    "Panniers & Mounts": 12500,
    "Windshield Kit": 3800,
}

# 5. Header Section
st.markdown(
    '<div class="hero-title">ROYAL ENFIELD</div>', unsafe_allow_html=True
)
st.markdown(
    '<div class="hero-subtitle">Official Customizer & Online Booking Studio</div>',
    unsafe_allow_html=True,
)

# 6. Main Layout Split
col_config, col_specs = st.columns([1.1, 0.9], gap="large")

with col_config:
    st.subheader("1. Select & Customize Model")

    selected_bike = st.selectbox(
        "Choose Model", list(bikes.keys()), index=0
    )
    bike_data = bikes[selected_bike]

    st.caption(f"_{bike_data['tagline']}_")

    col_var, col_paint = st.columns(2)
    with col_var:
        selected_variant = st.selectbox("Variant", bike_data["variants"])
    with col_paint:
        selected_paint = st.selectbox("Color Scheme", bike_data["paints"])

    st.subheader("2. Add Genuine Accessories")
    selected_accessories = []

    acc_cols = st.columns(2)
    for i, (acc_name, acc_price) in enumerate(accessories_catalog.items()):
        col_target = acc_cols[i % 2]
        if col_target.checkbox(f"{acc_name} (+₹{acc_price:,})"):
            selected_accessories.append((acc_name, acc_price))

with col_specs:
    st.subheader("📋 Specifications & Overview")
    
    st.info(f"**Model:** {selected_bike} | **Variant:** {selected_variant} | **Color:** {selected_paint}")

    with st.container(border=True):
        st.markdown("#### Engine & Technical Specs")
        for spec_key, spec_val in bike_data["specs"].items():
            st.write(f"**{spec_key}:** {spec_val}")

# 7. Price Calculation
base_val = bike_data["base_price"]
acc_total = sum(price for _, price in selected_accessories)
gst_tax = int((base_val + acc_total) * 0.18)
grand_total = base_val + acc_total + gst_tax

st.markdown("---")

# 8. Price Summary & EMI Calculator
col_price_summary, col_emi = st.columns([1, 1], gap="large")

with col_price_summary:
    st.subheader("💰 Price Breakdown")
    st.write(f"Base Price ({selected_bike}): **₹ {base_val:,}**")
    st.write(f"Accessories Total: **₹ {acc_total:,}**")
    st.write(f"Estimated Taxes & RTO (18%): **₹ {gst_tax:,}**")
    st.markdown(
        f"<div class='price-tag'>Estimated On-Road Price: ₹ {grand_total:,}</div>",
        unsafe_allow_html=True,
    )

with col_emi:
    st.subheader("🧮 EMI Calculator")
    down_payment = st.slider(
        "Down Payment (₹)",
        min_value=20000,
        max_value=int(grand_total * 0.8),
        value=50000,
        step=5000,
    )
    tenure_months = st.selectbox(
        "Loan Tenure (Months)", [12, 24, 36, 48, 60], index=2
    )
    interest_rate = 9.5

    loan_amount = grand_total - down_payment
    monthly_interest = interest_rate / (12 * 100)
    emi = (
        loan_amount
        * monthly_interest
        * ((1 + monthly_interest) ** tenure_months)
    ) / (((1 + monthly_interest) ** tenure_months) - 1)

    st.metric(
        label="Estimated Monthly EMI",
        value=f"₹ {int(emi):,}/mo",
        delta=f"Loan Amount: ₹{loan_amount:,}",
    )

st.markdown("---")

# 9. Booking & Test Ride Tabs
tab_booking, tab_testdrive = st.tabs(
    ["📝 Reserve & Book Online", "🏍️ Schedule a Test Ride"]
)

with tab_booking:
    st.subheader("Complete Your Reservation")
    with st.form("booking_form", clear_on_submit=False):
        c1, c2 = st.columns(2)
        with c1:
            full_name = st.text_input("Full Name *")
            email = st.text_input("Email Address *")
        with c2:
            phone = st.text_input("Phone Number *")
            city = st.text_input("Preferred Dealership / City *")

        payment_option = st.radio(
            "Booking Token Amount",
            ["Full Payment", "Token Amount (₹ 5,000)"],
            horizontal=True,
        )

        submit_booking = st.form_submit_button("Confirm & Reserve Bike")

        if submit_booking:
            if full_name and phone and email and city:
                st.balloons()
                st.success(
                    f"🎉 Congratulations **{full_name}**! Your reservation for **{selected_bike} ({selected_variant} - {selected_paint})** has been placed."
                )
                st.info(
                    f"A booking confirmation email has been sent to **{email}**. Our dealership in **{city}** will contact you at **{phone}** within 24 hours."
                )
            else:
                st.error(
                    "Please fill in all required fields marked with * to complete the booking."
                )

with tab_testdrive:
    st.subheader("Book a Free Test Ride")
    with st.form("test_ride_form"):
        tr_name = st.text_input("Your Name")
        tr_phone = st.text_input("Contact Number")
        tr_date = st.date_input("Preferred Date")
        tr_time = st.time_input("Preferred Time")

        submit_tr = st.form_submit_button("Request Test Ride")

        if submit_tr:
            if tr_name and tr_phone:
                st.success(
                    f"Test ride scheduled for **{tr_name}** on **{tr_date} at {tr_time}** for the **{selected_bike}**!"
                )
            else:
                st.error("Please provide your Name and Contact Number.")