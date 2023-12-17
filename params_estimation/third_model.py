import numpy as np



class ParameterEstimation:

    def __init__(self, actual, stimulus, raf, mek, erk, praf, pmek,
                 perk, r1, r2, r3, r_1, r_2, r_3, time, num_iter, learning_rate=1e-4, threshold=1e-6):

        # Initialize input parameters
        self.actual = actual  # The actual concentration of ppErk1/2 derived from a graph in the article
        self.num_iter = num_iter
        self.stimulus = stimulus
        self.raf = raf
        self.mek = mek
        self.erk = erk
        self.praf = praf
        self.pmek = pmek
        self.perk = perk
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r_1 = r_1
        self.r_2 = r_2
        self.r_3 = r_3
        self.time = time  # Simulation time
        self.learning_rate = learning_rate
        self.threshold = threshold  # Threshold to stop optimization

        # Initialize variables for optimization
        self.r0 = None
        self.mse = []
        self.populations = []



    def mean_squared_error(self, predicted):

        squared_diff = np.power((self.actual - predicted), 2)
        mse = np.mean(squared_diff)

        return mse



    def simulate_concentration(self):

        steps = len(self.time)
        # Initialize arrays to store species concentrations
        stimulus = np.zeros(steps)
        raf = np.zeros(steps)
        mek = np.zeros(steps)
        erk = np.zeros(steps)
        praf = np.zeros(steps)
        pmek = np.zeros(steps)
        perk = np.zeros(steps)

        # Initialize initial concentrations
        stimulus[0] = self.stimulus
        raf[0] = self.raf
        mek[0] = self.mek
        erk[0] = self.erk
        praf[0] = self.praf
        pmek[0] = self.pmek
        perk[0] = self.perk

        # Iteratively update concentrations based on reactions
        for i in range(1, steps):

            # Calculate derivatives for each species
            d_stimulus = -self.r0 * stimulus[i-1] * raf[i-1]
            d_raf = -self.r0 * stimulus[i-1] * raf[i-1]
            d_mek = (self.r_1 * pmek[i-1]) - (self.r1 * praf[i-1] * pmek[i-1])
            d_erk = (self.r_2 * perk[i-1]) + (self.r_3 * perk[i-1]) - (self.r2 * pmek[i-1] * erk[i-1]) - (self.r3 * erk[i-1] * praf[i-1])
            d_praf = (self.r0 * stimulus[i-1] * raf[i-1]) + (self.r_1 * pmek[i-1]) + (self.r_3 * perk[i-1]) - (self.r1 * mek[i-1] * praf[i-1]) - (self.r3 * erk[i-1] * praf[i-1])
            d_pmek = (self.r1 * praf[i-1] * mek[i-1]) - (self.r_1 * pmek[i-1]) - (self.r2 * pmek[i-1] * erk[i-1])
            d_perk = (self.r2 * pmek[i-1] * erk[i-1]) + (self.r3 * praf[i-1] * erk[i-1]) - (self.r_3 * perk[i-1])

            # Update concentrations
            stimulus[i] = stimulus[i-1] + d_stimulus
            raf[i] = raf[i-1] + d_raf
            mek[i] = mek[i-1] + d_mek
            erk[i] = erk[i-1] + d_erk
            praf[i] = praf[i-1] + d_praf
            pmek[i] = pmek[i-1] + d_pmek
            perk[i] = perk[i-1] + d_perk

        # Store the concentrations in a dictionary
        population = {
            'Time': self.time,
            'Stimulus': stimulus,
            'Raf': raf,
            'Mek': mek,
            'Erk': erk,
            'pRaf': praf,
            'pMek': pmek,
            'pErk': perk
        }

        self.populations.append(population)

        return erk



    def gradient_descent(self, r0):

        # Initialize parameters
        self.r0 = r0

        mse_prev = np.inf  # initialize with a large number

        for _ in range(self.num_iter):

            # Simulate concentrations using current parameters
            predicted = self.simulate_concentration()

            # Calculate the mean squared error
            mse = self.mean_squared_error(predicted)
            self.mse.append(mse)

            # Check for convergence based on the threshold
            if abs(mse_prev - mse) < self.threshold:
                break

            gradient_r0 = -2 * np.mean((self.actual - predicted) * self.populations[-1]['Raf'] * self.populations[-1]['Stimulus'])

            # Update parameter using gradient descent
            self.r0 -= self.learning_rate * gradient_r0

            mse_prev = mse  # Update the previous MSE

        return self.r0, self.mse, self.populations




# Time
t = np.array([0, 100, 280, 420, 600, 840, 1800, 2400, 3000])
time = np.arange(0, 3001, 1)



# ppErk concentrations
erk_ngf = np.array([0, 0.19, 0.9, 1, 0.67, 0.55, 0.58, 0.5, 0.55])
erk_egf = np.array([0, 0.7, 1.0, 0.41, 0.1, 0.03, 0.01, 0.01, 0.01])

actual_ngf = np.interp(time, t, erk_ngf)
actual_egf = np.interp(time, t, erk_egf)


num_iter = 1000



# Initial Concentration of Species
ngf = 50
egf = 100
raf = 1
mek = 1
erk = 1
pRaf = 0
pMek = 0
pErk = 0




# Parameters
nr1 = 6.18
nr2 = 0.63
nr3 = 0.96
nr_1 = -0.17
nr_2 = -3.73
nr_3 = 0.4

er1 = 1.11
er2 = 1
er3 = 0.09
er_1 = -0.1
er_2 = -0.35
er_3 = -0.53




ngf_model = ParameterEstimation(actual_ngf, ngf, raf, mek, erk, pRaf, pMek, pErk, nr1, nr2, nr3, nr_1, nr_2, nr_3, time, num_iter)
egf_model = ParameterEstimation(actual_egf, egf, raf, mek, erk, pRaf, pMek, pErk, er1, er2, er3, er_1, er_2, er_3, time, num_iter)


r0, mse, populations = ngf_model.gradient_descent(r0=1)
r0, mse, populations = egf_model.gradient_descent(r0=1)





