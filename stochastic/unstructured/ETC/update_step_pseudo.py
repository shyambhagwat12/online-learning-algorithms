def update_step_pseudo(avg, m, num_iter, num_inst):
    reg = np.zeros((num_inst, num_iter))
    algo = ETC(avg, m)
    #Number of epochs
    for j in range(num_inst):
        algo.restart()
        
        if (j+1)%10 == 0:
            print('Instance number = ', j+1)
        #iterate upto to horizon
        for t in range(num_iter-1):
            #get round robin reward
            rew_vec = get_reward(avg)
            #For explore - less than m*t - choose current arm
            if algo.time < algo.num_arms * algo.m:
                arm = int(algo.time % algo.num_arms)
                algo.time += 1.0
                algo.num_pulls[arm] += 1
                algo.emp_means[arm] += (rew_vec[arm] - algo.emp_means[arm])/algo.num_pulls[arm]
            else:
            #else if exploit - choose best arm
                arm = np.argmax(algo.emp_means)
            algo.regret += algo.means[algo.best_arm] - algo.means[arm]
            reg[j,t]= np.asarray(algo.regret)
    return reg