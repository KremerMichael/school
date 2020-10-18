from batteries import * #For definitions of batteries


class Battery:

    #Variables for storing battery specific information
    charge = 0 #kWh

    #Constants to define battery behavior
    MAX_CHARGE           = tesla_powerwall_2['TOTAL_ENERGY']         #kWh
    USABLE_CHARGE        = tesla_powerwall_2['USABLE_ENERGY']        #kWh
    MAX_CONTINUOUS       = tesla_powerwall_2['MAX_CONTINUOUS']       #kVA
    STORAGE_EFFICIENCY   = tesla_powerwall_2['STORAGE_EFFICIENCY']   #No unit (decimal)
    DEPLETION_EFFICIENCY = tesla_powerwall_2['DEPLETION_EFFICIENCY'] #No unit (decimal)

    #Function to charge battery based on some formula
    #energy in kWh
    def addCharge(self, energy):
        self.charge += (energy * self.STORAGE_EFFICIENCY) #some formula for charging here
        #should this return the estimated cost of this charge?

    #Function to drain battery based on some formula
    #Time in units of hours
    def drainCharge(self, time):
        self.charge -= time * self.DEPLETION_EFFICIENCY#some formula for depletion here

        #https://www.eia.gov/beta/electricity/gridmonitor/dashboard/electric_overview/regional/REG-MIDW
