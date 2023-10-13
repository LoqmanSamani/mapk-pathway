import numpy as np


class ParameterEstimation:

    def __init__(self, actual_perk, num_iterations, stimuli, raf, mek, erk, praf, pmek,
                 perk, r1, r2, r3, r_1, r_2, r_3, time, learning_rate=1e-3, threshold=1e-6):

        # Initialize input parameters
        self.actual_perk = actual_perk
        self.num_iterations = num_iterations
        self.stimuli = stimuli
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
        self.r4 = None
        self.r0 = None
        self.mse = None
        self.populations = None  # a variable to store the concentration of the species in the last iteration

    def mean_squared_error(self, simulated_erk):

        """
        Calculates the mean squared error (MSE) between
        the actual and simulated concentrations.
        Args:
            simulated_erk (numpy.ndarray): Simulated
            concentrations of pErk.

        Returns:
            float: The MSE between actual and
            simulated concentrations.
        """

        squared_diff = np.power((self.actual_perk - simulated_erk), 2)

        mse = np.mean(squared_diff)

        return mse

    def simulate_concentration(self):

        """
        Simulates the concentrations of various species
        over time based on biochemical reactions.

        Returns:
            numpy.ndarray: Simulated concentrations of pErk.
        """

        # Initialize arrays to store species concentrations
        stimuli_concentration = np.zeros(len(self.time))
        raf_concentration = np.zeros(len(self.time))
        mek_concentration = np.zeros(len(self.time))
        erk_concentration = np.zeros(len(self.time))
        praf_concentration = np.zeros(len(self.time))
        pmek_concentration = np.zeros(len(self.time))
        perk_concentration = np.zeros(len(self.time))

        # Initialize initial concentrations
        stimuli_concentration[0] = self.stimuli
        raf_concentration[0] = self.raf
        mek_concentration[0] = self.mek
        erk_concentration[0] = self.erk
        praf_concentration[0] = self.praf
        pmek_concentration[0] = self.pmek
        perk_concentration[0] = self.perk

        """
        The concentration of each species will be updated (dynamic programming) based on the reaction-information below.

             **REACTIONS**       **RATE EQUATIONS**         **RARE OF CHANGE**
        R1: EGF + Raf -> pRaf      r0 * EGF * Raf
        R2: pRaf + Mek -> pMek     r1 * pRaf * Mek           dEGF/dt = - r0 * EGF * Raf 
        R3: pMek + pRaf -> Raf     r_1 * pMek * pRaf         dRaf/dt = (r_1 * pMek * pRaf) +(r_3 * pErk * pRaf)-(r0 * EGF * Raf)
        R4: pMek + Erk -> pErk     r2 * pMek * Erk           dmek/dt = (r_2 * pErk * pMek)-(r1 * pRaf * Mek)
        R5: pErk + pMek -> Mek     r_2 * pErk * pMek         dErk/dt = (r4 * pErk)-(r3 * pRaf * Erk)-(r2 * pMek * Erk)
        R6: pRaf + Erk -> pErk     r3 * pRaf * Erk           dpRaf/dt = (r0 * EGF * Raf)-(r_1 * pMek * pRaf)-(r3 * pRaf * Erk)-(r_3 * pErk * pRaf)
        R7: pErk + pRaf -> Raf     r_3 * pErk * pRaf         dpMek/dt = (r1 * pRaf * Mek)-(r_1 * pMek * pRaf)-(r2 * pMek * Erk)-(r_2 * pErk * pMek)
        R8: pErk -> Erk            r4 * pErk                 dpErk/dt = (r2 * pMek * Erk)-(r_2 * pErk * pMek)+(r3 * pRaf * Erk)-(r_3 * pErk * pRaf)-(r4 * pErk)

        """

        # Iteratively update concentrations based on reactions
        for i in range(1, len(self.time)):
            # Calculate derivatives for each species
            der_stimuli = -self.r0 * stimuli_concentration[i - 1] * raf_concentration[i - 1]
            der_raf = (self.r_1 * pmek_concentration[i - 1] * praf_concentration[i - 1]) + (
                        self.r_3 * perk_concentration[i - 1] * praf_concentration[i - 1]) - (
                                  self.r0 * stimuli_concentration[i - 1] * raf_concentration[i - 1])
            der_mek = (self.r_2 * perk_concentration[i - 1] * pmek_concentration[i - 1]) + (
                        self.r1 * praf_concentration[i - 1] * pmek_concentration[i - 1])
            der_erk = (self.r4 * perk_concentration[i - 1]) - (
                        self.r3 * praf_concentration[i - 1] * erk_concentration[i - 1] - (
                            self.r2 * pmek_concentration[i - 1] * erk_concentration[i - 1]))
            der_praf = (self.r0 * stimuli_concentration[i - 1] * raf_concentration[i - 1]) - (
                        self.r_1 * pmek_concentration[i - 1] * praf_concentration[i - 1]) - (
                                   self.r3 * praf_concentration[i - 1] * erk_concentration[i - 1] - (
                                       self.r_3 * perk_concentration[i - 1] * praf_concentration[i - 1]))
            der_pmek = (self.r1 * praf_concentration[i - 1] * mek_concentration[i - 1]) - (
                        self.r_1 * pmek_concentration[i - 1] * praf_concentration[i - 1]) - (
                                   self.r2 * pmek_concentration[i - 1] * erk_concentration[i - 1]) - (
                                   self.r_2 * perk_concentration[i - 1] * pmek_concentration[i - 1])
            der_perk = (self.r2 * pmek_concentration[i - 1] * erk_concentration[i - 1]) - (
                        self.r_2 * perk_concentration[i - 1] * pmek_concentration[i - 1]) + (
                                   self.r3 * praf_concentration[i - 1] * erk_concentration[i - 1]) - (
                                   self.r_3 * perk_concentration[i - 1] * praf_concentration[i - 1]) - (
                                   self.r4 * perk_concentration[i - 1])

            # Update concentrations
            stimuli_concentration[i] = stimuli_concentration[i - 1] + der_stimuli
            raf_concentration[i] = raf_concentration[i - 1] + der_raf
            mek_concentration[i] = mek_concentration[i - 1] + der_mek
            erk_concentration[i] = erk_concentration[i - 1] + der_erk
            praf_concentration[i] = praf_concentration[i - 1] + der_praf
            pmek_concentration[i] = pmek_concentration[i - 1] + der_pmek
            perk_concentration[i] = perk_concentration[i - 1] + der_perk

        # Store the concentrations in a dictionary
        self.populations = {
            'Time': self.time,
            'Stimuli': stimuli_concentration,
            'Raf': raf_concentration,
            'Mek': mek_concentration,
            'Erk': erk_concentration,
            'pRaf': praf_concentration,
            'pMek': pmek_concentration,
            'pErk': perk_concentration
        }

        return perk_concentration

    def gradient_descent(self):

        """
        Perform gradient descent to optimize parameters 'r4' and 'r0'.

            Returns:
                float: Estimated 'r4'.
                float: Estimated 'r0'.
                float: Final MSE after optimization.
                dict: Concentrations of species over time.
        """

        # Initialize parameters
        self.r4 = 0.5
        self.r0 = 1

        mse_prev = np.inf  # initialize with a large number

        for iteration in range(self.num_iterations):

            # Simulate concentrations using current parameters
            simulated_erk = self.simulate_concentration()

            # Calculate the MSE
            mse = self.mean_squared_error(simulated_erk)
            self.mse = mse

            # Check for convergence based on the threshold
            if abs(mse_prev - mse) < self.threshold:
                break

            # Calculate the gradients (partial derivatives) of MSE with respect to 'r4' and 'r0'
            gradient_r4 = -2 * np.mean((self.actual_perk - simulated_erk) * self.populations['pErk'])
            gradient_r0 = -2 * np.mean(
                (self.actual_perk - simulated_erk) * self.populations['pRaf'] * self.populations['Stimuli'])

            # Update parameters using gradient descent
            self.r4 -= self.learning_rate * gradient_r4
            self.r0 -= self.learning_rate * gradient_r0

            mse_prev = mse  # Update the previous MSE

        return self.r4, self.r0, self.mse, self.populations
