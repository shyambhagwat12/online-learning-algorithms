def pseudo(REPEAT, HORIZON):
  LinUCB_history = np.zeros(HORIZON)
  my_context_arm = context_arm()
  for rep in tqdm(range(REPEAT)):
    
    algo = LinUCB(available_arms)
    for i in range(HORIZON):
      max_score = -1
      max_index = -1
      max_arm = []
      for arm_index in range(algo.num_arms):
            V_inv = np.linalg.inv(algo.V)
            algo.theta = np.dot(V_inv, algo.b)
            ucb_score = np.dot(algo.theta.T, algo.arms[arm_index] ) + algo.alpha * np.sqrt(np.dot(algo.arms[arm_index].T, np.dot(V_inv, algo.arms[arm_index] )))
            if ucb_score > max_score:
                max_score = ucb_score
                max_arm = arm_index
                max_arm = algo.arms[arm_index]
      reward = my_context_arm.pull_arm(max_arm)
      algo.reward_history.append(reward)
      algo.V += np.outer(algo.arms[max_arm], algo.arms[max_arm].T)
      x= algo.arms[max_arm].reshape(4,1)
      algo.b += reward * x
    LinUCB_history += np.array(algo.reward_history)

  LinUCB_expected_reward = LinUCB_history / REPEAT
  LinUCB_expected_reward = np.cumsum(LinUCB_expected_reward)
  best_rewards = my_context_arm.genie_reward()
  best_rewards = best_rewards * np.linspace(1, HORIZON, num=HORIZON)
  LinUCB_regret = best_rewards - LinUCB_expected_reward
  return LinUCB_regret