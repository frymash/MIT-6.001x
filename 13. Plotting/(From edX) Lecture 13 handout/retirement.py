# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:28:55 2016

@author: ericgrimson
"""

import pylab as plt

# retire() calculates savings compounded by interest
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    monthlyRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1 + monthlyRate) + monthly]
    return base, savings

# display graph of savings given different monthly deposits
def displayRetirementWithMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:'+  str(monthly))
        plt.legend(loc = 'upper left')

displayRetirementWithMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40* 12) # 40 years of deposits

# display graph of savings given different rates of interest
def displayRetirementWithRates(monthly, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, 
                 label = 'retire:'+str(monthly)+ ':' + str(int(rate*100)))
        plt.legend(loc = 'upper left')

displayRetirementWithRates(800,[.03, .05, .07], 40*12)

'''
# display graph of savings given a. different monthly deposits and b. different monthly deposits
def displayRetirementWithMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals,
                     label = 'retire:'+str(monthly)+ ':' + str(int(rate*100)))
            plt.legend(loc = 'upper left')
            
displayRetirementWithMonthsAndRates([500, 700, 900, 1100], 
                                    [.03, .05, .07], 40*12)
'''

# display graph of savings given a. different monthly deposits and b. different monthly deposits
# BUT with better visualisation as compared to the other def of this func shown above
def displayRetirementWithMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--', '^']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)] 
        # "i % len(monthLabels)" mean that the colours in monthLabel will repeat every 4 monthlies. this is a very, very nifty trick.
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            # similarly to line 70, "j % len(rateLabels)" mean that the graph styles in rateLabels will repeat every 4 rates.
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel+rateLabel,
                     label = 'retire:'+str(monthly)+ ':' + str(int(rate*100)))
            plt.legend(loc = 'upper left')

displayRetirementWithMonthsAndRates([500, 700, 900, 1100], 
                                   [.03, .05, .07], 40*12)


plt.show()
  

        