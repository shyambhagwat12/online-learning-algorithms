def pseudo_code_egreedy(avg, num_iter, num_inst):
        reg = np.zeros((num_inst, num_iter))
        algo = egreedy(avg)
        algo.regret = 0.0
        for j in range(num_inst-1):
            algo.restart()
            if (j+1)%10 == 0:
                print('Instance number = ', j+1)
      
            for l in range(num_iter-1):
                rew_vec = get_reward(avg)
                zt = np.random.binomial(1, algo.eps) 
                if zt == 1:
                  arm=np.random.choice(algo.num_arms, size=(1), replace=True)
                  algo.num_pulls[arm] += 1
                  algo.emp_means[arm] += (rew[arm] - algo.emp_means[arm])/algo.num_pulls[arm]
                  algo.time += 1
                  algo.eps = min(1,(algo.num_arms*algo.C)/(algo.time * (algo.delta**2))
                else:
                  arm=np.argmax(algo.emp_means/algo.num_pulls
                algo.regret += algo.means[algo.best_arm] - algo.means[arm]
                reg[j,l]= np.asarray(algo.regret)
        return reg

