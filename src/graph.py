import matplotlib.pyplot as pyplot
from matplotlib.ticker import FormatStrFormatter
import datetime

def plot(independent_variable_name, dependent_variable_name, independent_variable_values, dependent_variable_values, predictions = None):
    if isinstance(independent_variable_values[0], datetime.date) or isinstance(independent_variable_values[0], datetime.datetime):
        pyplot.plot_date(independent_variable_values, dependent_variable_values, marker='o')
    else:
        pyplot.scatter(independent_variable_values, dependent_variable_values, s=10)
    pyplot.xlabel(independent_variable_name)
    pyplot.ylabel(dependent_variable_name)
    if predictions != None: pyplot.plot(independent_variable_values, predictions, color='r')
    pyplot.gca().yaxis.set_major_formatter(FormatStrFormatter('%.0f')) # this prevents use of e notation
    pyplot.show()