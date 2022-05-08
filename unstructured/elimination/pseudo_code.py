def pseudo_code(avg, num_iter, num_inst):
    reg = np.zeros((num_inst, num_iter))
    algo = Elimination(avg, num_iter)
    for k in range(num_inst):  
        algo.cum_reg = [
        algo.m = 10   
        algo.time = 0.0
        algo.delta = 
        while len(algo.cum_reg) <= num_iter:
            if len(algo.cum_reg) >= num_iter:
                break   
            for t in range(int(algo.m) * algo.A.size)
              if len(algo.cum_reg) >= num_iter:
                break 
              else:
                rew_vec = get_reward(avg)
                algo.iterate(rew_vec)   
            algo.update_elim()
            algo.restart()
            algo.time += 1
            algo.m = (2* np.log(algo.num_iter  * np.square(algo.delta)))  / np.square(algo.delta)
            algo.delta = algo.delta/2
        reg[k,:]= np.asarray(algo.cum_reg)

    return reg


def update_elim(self):
      confidence = np.sqrt(np.log(self.num_iter  * np.square(self.delta))  / (2*self.m))
      i=0
      if len(self.A) == 1:
          return None 
      for i in range(len(self.A)):
        all_possible=self.emp_means.copy()
        all_possible= np.delete(all_possible, i) 
        all_possible = all_possible -confidence
        best_possible = self.emp_means[i] + confidence
        rest = np.max(all_possible )
        if (best_possible) < rest:
          self.A = np.delete(self.A, i)
          break;
        else:
          pass
      return None