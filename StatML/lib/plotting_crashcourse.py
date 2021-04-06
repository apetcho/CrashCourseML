#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import wraps

import seaborn as sns


def title(msg):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            n = len(msg)
            dash = '*' * n
            print(f"\n{dash}\n{msg}\n{dash}\n\n")
            ans = func(*args, **kwargs)
            if ans is None:
                return
            return ans
        return wrapper
    return decorate
    

@title("Basic Plots")
def basic_plot():
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    z = np.cos(x)
    plt.figure()
    plt.plot(x, y, label='sinus', color='blue', linestyle='--', linewidth=2)
    plt.plot(x, z, label='cosinus', color='red', linestyle='--', linewidth=2)
    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.title("Title")
    plt.legend()
    plt.show()
    

@title("Scatter 2D Plots")
def scatter_2d_plots():
    np.random.seed(2021)
    data = np.random.randn(2, 100)
    plt.scatter(data[0], data[1])
    plt.title("Scatter 2D Plot")
    plt.show()


@title("Plotting with keyword strings")
def plotting_with_keyword_strings():
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10*np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100
    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.show()
    

@title("Plotting with categorial variables")
def plotting_with_categorial_variables():
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]
    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorial Plotting')
    plt.show()  


@title("Working with text")
def working_with_text():
    mu, sigma = 100, 15
    np.random.seed(2021)
    x = mu + sigma * np.random.randn(10000)
    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
    
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Historgram of IQ')
    plt.text(60, 0.025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()
    
    
class SeabornTutorial:
    """Quick seaborn plotting package tutorial."""
    
    @title("Seaborn: different scatter variables")
    def different_scatter_varibales(self):
        sns.set_theme(style='whitegrid')
        diamonds = sns.load_dataset('diamonds')
        fig, ax = plt.subplots(figsize=(6.5, 6.5))
        sns.despine(fig, left=True, bottom=True)
        clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
        sns.scatterplot(x="carat", y="price",
                        hue="clarity", size="depth",
                        palette="ch:r=-.2,d=.3_r",
                        hue_order=clarity_ranking,
                        sizes=(1, 8), linewidth=0,
                        data=diamonds, ax=ax)
        plt.show()
    
    @title("Seaborn: heat scatter")
    def heat_scatter(self):
        sns.set_theme(style='whitegrid')
        df = sns.load_dataset("brain_networks",
                              header=[0, 1, 2], index_col=0)
        used_networks = [1, 5, 6, 7, 8, 12, 13, 17]
        used_columns = (df.columns
                        .get_level_values("network")
                        .astype(int)
                        .isin(used_networks))
        df = df.loc[:, used_columns]

        df.columns = df.columns.map("-".join)
        # Compute a correlation matrix and convert to long-form
        corr_mat = df.corr().stack().reset_index(name='correlation')
        # Draw each cell as a scatter point with varying size and color
        g = sns.relplot(
            data=corr_mat,
            x='level_0', y='level_1', hue='correlation',
            size='correlation', palette='vlag', hue_norm=(-1, 1),
            edgecolor='.7', height=10, sizes=(50, 250),
            size_norm=(-.2, .8),
        )
        
        # Tweak the figure to finalize
        g.set(xlabel='', ylabel='', aspect='equal')
        g.despine(left=True, bottom=True)
        g.ax.margins(.02)
        for label in g.ax.get_xticklabels():
            label.set_rotation(90)
        for artist in g.legend.legendHandles:
            artist.set_edgecolor('.7')

        plt.show()
    
    @title("Seaborn: timeseries facets")
    def timeseries_facets(self):
        sns.set_theme(style='dark')
        flights = sns.load_dataset('flights')
        
        # Plot each year's time series in its own facet
        g = sns.relplot(
            data=flights,
            x='month', y='passengers', col='year', hue='year',
            kind='line', palette='crest', linewidth=4, zorder=5,
            col_wrap=3, height=2, aspect=1.5, legend=False,
        )
        
        # Iterate over each supblot to customise further
        for year, ax in g.axes_dict.items():
            # Add the title as an annotation withing the plot
            ax.text(.8, .85, year, transform=ax.transAxes, fontweight='bold')
            # Plot every year's time series in the background
            sns.lineplot(
                data=flights, x='month', y='passengers', units='year',
                estimator=None, color='.7', linewidth=1, ax=ax,
            )
        ax.set_xticks(ax.get_xticks()[::2])
        g.set_titles("")
        g.set_axis_labels("", "Passengers")
        g.tight_layout()
        plt.show()
        
    def __call__(self, which='heat_scatter'):
        if which == 'heat_scatter':
            self.heat_scatter()
        if which == 'different_scatter':
            #self.different_scatter_variables()
            self.different_scatter_varibales()
        if which == 'timeseries':
            self.timeseries_facets()
        #plt.show()


def main():
    # basic_plot()
    # scatter_2d_plots()
    # plotting_with_keyword_strings()
    # plotting_with_categorial_variables()
    # working_with_text()
    
    #import threading
    import multiprocessing
    
    thrds = []
    tutos = ('heat_scatter', 'different_scatter', 'timeseries')
    for tuto in tutos:
        #t = threading.Thread(target=SeabornTutorial(), args=(tuto,))
        t = multiprocessing.Process(target=SeabornTutorial(), args=(tuto,))
        t.start()
        thrds.append(t)
        
    for t in thrds:
        t.join()
        
    #plt.show()
    
    #sns_tuto = SeabornTutorial()
    #tutos = ('heat_scatter', 'different_scatter', 'timeseries')
    #for tuto in tutos:
    #    sns_tuto(tuto)
        
    
if __name__ == "__main__":
    main()