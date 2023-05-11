def mining_profitability_calculator():
    # User Inputs
    hashrate = float(input("Enter your Hashrate (MH/s): "))
    power_consumption = float(input("Enter your Power Consumption (W): "))
    cost_per_kwh = float(input("Enter your Cost per KWh ($): "))
    pool_fee = float(input("Enter your Pool Fee (%): "))

    # Constants
    reward_per_block = 2  # for Ethereum as of the time of writing
    seconds_in_day = 86400
    eth_to_usd = 3000  # for Ethereum as of the time of writing

    # Calculate
    power_cost_per_day = (power_consumption / 1000) * cost_per_kwh * 24
    eth_mined_per_day = (hashrate * seconds_in_day * reward_per_block) / (1e9 * pool_fee)
    revenue_per_day = eth_mined_per_day * eth_to_usd
    profit_per_day = revenue_per_day - power_cost_per_day

    # Display Results
    print(f"Daily Profit: ${profit_per_day}")
    print(f"Monthly Profit: ${profit_per_day * 30}")
    print(f"Yearly Profit: ${profit_per_day * 365}")

# Run the calculator
mining_profitability_calculator()
