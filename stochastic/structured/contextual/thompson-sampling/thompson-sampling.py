def pseudo(avg, num_iter, num_inst):
    reg = np.zeros((num_inst, num_iter))   
    algo = TS(avg)
    for k in range(num_inst):
        algo.restart()
  
        if (k+1)%10 == 0:
            print('Instance number = ', k+1)
        for t in range(num_iter-1):
            rew_vec = get_reward(avg)
            
            arm = algo.get_best_arm()
            if(rew_vec[arm]==1):
                algo.alpha[arm] = algo.alpha[arm] + 1
            else:
                algo.beta[arm] = algo.beta[arm] + 1
            algo.means = np.random.beta(algo.alpha , algo.beta)
            algo.update_reg(arm,rew_vec)
            
        reg[k,:] = np.asarray(algo.cum_reg)
        
    return reg