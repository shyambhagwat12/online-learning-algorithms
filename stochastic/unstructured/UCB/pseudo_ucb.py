    def pseudo(self, rew_vec):  ## Iterate the algorithm
        arm = self.get_best_arm() 
        self.time += 1.0
        self.num_pulls[arm] += 1.0
        self.emp_means[arm] = (self.emp_means[arm] * (self.num_pulls[arm] - 1.0) + rew_vec[arm])/self.num_pulls[arm]
        self.update_reg(rew_vec, arm)
        ft= 1 + (self.time * np.square(np.log(self.time)))
        self.ucb_arr[arm] = self.emp_means[arm] + np.sqrt( (2* np.log(ft)) / self.num_pulls[arm] )
        return None