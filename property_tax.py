# Part 1: Property Taxes

def tax():
    assess_value = assessment_value()
    # Since the asssessment value is 82 cents per $100 for the assessment value
    # the calculation for the tax is as follows
    property_tax = (assess_value/100)*.82
    print(f'The property tax on this property is ${property_tax:,.2f}.')
def assessment_value():
    property_value = float(input('Value of the property: '))
    # To calculate the assessment value the overall value of the property is
    # multiplied by 6%
    assessment_amount = property_value*.06
    return assessment_amount
tax()
