def pseudo_exp3(avg, eta, num_iter, num_inst, var):
    
    reg = np.zeros((num_inst, num_iter))  
    algo = EXP3(avg, eta)
    for k in range(num_inst):
        algo.restart()
        
        if (k+1)%10 == 0:
            print('Instance number = ', k+1)
        for t in range(num_iter-1):
            rew_vec = get_reward(avg,var)
            arm = np.random.choice(algo.num_arms,1,p=algo.probs_arr)
            algo.num_pulls[arm] += 1.0
            algo.emp_means[arm] +=  rew_vec[arm]/algo.probs_arr[arm]
            algo.probs_arr = np.exp(algo.eta * algo.emp_means) / np.sum(np.exp(algo.eta * algo.emp_means))
            algo.update_reg(arm,rew_vec)
        reg[k,:] = np.asarray(algo.cum_reg)
        
    return reg