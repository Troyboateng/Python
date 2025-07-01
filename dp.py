def maximize_walking_time(plan):
    n = len(plan)
    A = [0] * (n + 1)  # Initialize the DP array

    # Fill the DP array from the end to the beginning
    for i in range(n - 1, -1, -1):
        t_i, r_i = plan[i]
        if i + r_i + 1 < n:
            A[i] = max(t_i + A[i + r_i + 1], A[i + 1])
        else:
            A[i] = max(t_i, A[i + 1])
    
    # Find the optimal walking days
    i = 0
    optimal_days = []
    while i < n:
        t_i, r_i = plan[i]
        if i + r_i + 1 < n and A[i] == t_i + A[i + r_i + 1]:
            optimal_days.append(i + 1)  # Day is 1-indexed
            i += r_i + 1
        elif A[i] == t_i:
            optimal_days.append(i + 1)  # Day is 1-indexed
            break
        else:
            i += 1

    return A, optimal_days

def verify_statements(plan):
    A, optimal_days = maximize_walking_time(plan)
    max_time = A[0]

    # Print the dynamic programming array and optimal days
    print(f"A: {A}")
    print(f"Optimal walking days: {optimal_days}")
    print(f"Maximum walking time: {max_time}")

    # Statements
    r2 = plan[1][1]
    statement_1 = r2 == 3

    A3 = A[3] if len(A) > 3 else None
    statement_2 = A3 == 90

    A4 = A[4] if len(A) > 4 else None
    A5 = A[5] if len(A) > 5 else None
    statement_3 = A4 == A5

    statement_4 = max_time > 200

    # Check if Alice can achieve maximum time even if she skips the first 2 days
    new_plan = plan[2:]
    new_max_time = maximize_walking_time(new_plan)
    statement_5 = new_max_time < max_time

    # Check if Alice must walk on day 3 to achieve the optimal time
    statement_6 = 3 in optimal_days

    # Check for at least 2 optimal ways
    statement_7 = len(set(optimal_days)) >= 2

    # Check if adding 15 minutes on day 0 increases the optimal time
    plan[0][0] += 15
    new_max_time, _ = maximize_walking_time(plan)
    statement_8 = new_max_time > max_time

    # Print results
    print(f"1. r2 = 3: {'Selected' if statement_1 else 'Not selected'}. r2 = {r2}")
    print(f"2. A(3) = 90: {'Selected' if statement_2 else 'Not selected'}. A(3) = {A3}")
    print(f"3. A(4) = A(5): {'Selected' if statement_3 else 'Not selected'}. A(4) = {A4}, A(5) = {A5}")
    print(f"4. Alice can walk more than 200 minutes with this plan: {'Selected' if statement_4 else 'Not selected'}")
    print(f"5. Alice can achieve the maximum walking time even if she skips walking on the first 2 days: {'Selected' if statement_5 else 'Not selected'}")
    print(f"6. Alice must walk on day 3 to achieve her optimal walking time: {'Selected' if statement_6 else 'Not selected'}")
    print(f"7. There are at least 2 optimal ways that Alice can plan for her walk to have maximum walking time: {'Selected' if statement_7 else 'Not selected'}")
    print(f"8. If Alice intends to walk 15 minutes more on day 0, her optimal walking time will increase 15 minutes: {'Selected' if statement_8 else 'Not selected'}")

# Example usage:
plan = [[45, 2], [90, 1], [45, 2], [75, 1], [75, 1], [75, 1], [75, 2]]
verify_statements(plan)
