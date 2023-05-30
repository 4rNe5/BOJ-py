def dhondt(n, m, s):
  """
  Computes the minimum and maximum votes for each party in the JAG Kingdom election.

  Args:
    n: The total number of valid votes.
    m: The number of parties.
    s: The number of seats won by each party.

  Returns:
    A list of tuples, where each tuple contains the minimum and maximum votes for each party.
  """

  # Check if the given situation is possible.
  if sum(s) > n:
    return "impossible"

  # Initialize the votes for each party.
  votes = [0] * m

  # Iterate over the parties.
  for i in range(m):
    # Compute the quota for each party.
    quota = n / (m + 1) * s[i]

    # Assign votes to each party until the quota is met.
    while votes[i] < quota:
      votes[i] += 1

  # Return the minimum and maximum votes for each party.
  return [(votes[i] - 1, votes[i]) for i in range(m)]


if __name__ == "__main__":
  # Read the input.
  n, m = map(int, input().split())
  s = list(map(int, input().split()))

  # Compute the minimum and maximum votes for each party.
  results = dhondt(n, m, s)

  # Print the results.
  if results == "impossible":
    print("impossible")
  else:
    for result in results:
      print(*result)
