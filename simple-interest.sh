
#!/usr/bin/env bash
# simple-interest.sh - Calculate simple interest for given principal, rate, and time
# Usage: bash simple-interest.sh <principal> <rate> <time>

# Function to display usage information
display_usage() {
  echo "Usage: $0 <principal> <annual_rate_percent> <time_years>"
  echo
  echo "  principal            The principal amount (e.g., 1000)"  
  echo "  annual_rate_percent  The annual interest rate in percent (e.g., 5 for 5%)"  
  echo "  time_years           The time period in years (e.g., 2)"  
  exit 1
}

# Check for correct number of arguments
if [ "$#" -ne 3 ]; then
  echo "Error: Incorrect number of arguments."
  display_usage
fi

PRINCIPAL=$1
RATE=$2
TIME=$3

# Validate that inputs are numbers
test_number() {
  local re='^[0-9]+([.][0-9]+)?$'
  if ! [[ $1 =~ $re ]]; then
    echo "Error: '$1' is not a valid number."
    exit 1
  fi
}

# Validate inputs
for val in "$PRINCIPAL" "$RATE" "$TIME"; do
  test_number "$val"
done

# Calculate simple interest
# Formula: Simple Interest = (P * R * T) / 100
INTEREST=$(awk "BEGIN { printf \"%.2f\", ($PRINCIPAL * $RATE * $TIME) / 100 }")

# Calculate total amount
total_amount=$(awk "BEGIN { printf \"%.2f\", $PRINCIPAL + $INTEREST }")

# Output results
echo "Principal amount: $PRINCIPAL"
echo "Annual interest rate: $RATE%"
echo "Time period: $TIME years"
echo "Simple interest: $INTEREST"
echo "Total amount after $TIME years: $total_amount"
