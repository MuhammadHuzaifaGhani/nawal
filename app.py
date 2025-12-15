import streamlit as st

st.title("📊 List Analyzer App")
st.write("Enter numbers separated by commas (example: 10, 25, 3, 7)")

user_input = st.text_input("Enter your numbers:")

if st.button("Analyze List"):
    try:
        numbers = [float(num.strip()) for num in user_input.split(",")]

        if len(numbers) == 0:
            st.warning("Please enter at least one number.")
        else:
            largest = max(numbers)
            smallest = min(numbers)
            total_sum = sum(numbers)

            st.success("✅ Analysis Complete!")
            st.write(f"🔹 Numbers List: {numbers}")
            st.write(f"🔺 Largest Number: {largest}")
            st.write(f"🔻 Smallest Number: {smallest}")
            st.write(f"➕ Sum of Numbers: {total_sum}")

    except ValueError:
        st.error("❌ Please enter only numbers separated by commas.")
