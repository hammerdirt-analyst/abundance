import matplotlib.pyplot as plt
from utilities.utility_functions import make_stacked_blocks as make_stacked_blocks
from utilities.utility_functions import save_the_figure as save_the_figure
from utilities.utility_functions import make_blocks
import numpy as np


def stackedBarChart(**kwargs):

    fig, ax = plt.subplots(figsize=(3,6))

    total_quant = kwargs['a_df'].quantity.sum()

    y_limit = total_quant
    y_max = y_limit + 2
    the_percent = total_quant*kwargs['percent']

    kwargs['the_title']["label"] = "{},  total={:,}".format(kwargs['the_title']["label"], total_quant)
    kwargs['the_sup_title']["label"] = '{}, {} - {}'.format(kwargs['the_sup_title']["label"], kwargs['min_date'], kwargs['max_date'])

    the_bottom = 0
    the_data = make_blocks(kwargs['a_df'],
                           the_percent,
                           kwargs['date_range'],
                           total_quant,
                           kwargs['code_dict']
                          )
    color_map = plt.cm.get_cmap(kwargs['color_map'],100)
    color=iter(color_map(np.linspace(.2,.75,len(the_data))))

    make_stacked_blocks(the_data, ax, color)

    plt.ylabel(kwargs['y_axis']['label'],
               fontfamily=kwargs['y_axis']['fontfamily'],
               labelpad=kwargs['y_axis']['lablepad'],
               color=kwargs['y_axis']['color'],
               size=kwargs['y_axis']['size']
              )

    plt.xlabel(kwargs['x_axis']['label'],
               fontfamily=kwargs['x_axis']['fontfamily'],
               labelpad=kwargs['x_axis']['lablepad'],
               color=kwargs['x_axis']['color'],
               size=kwargs['x_axis']['size'],
               ha='left',
               x=0
              )

    plt.subplots_adjust(**kwargs['subplot_params'])

    plt.xticks([0])
    plt.ylim(0, y_max)

    plt.title(**kwargs['the_title'], fontdict=kwargs['title_style'], **kwargs['the_title_position'])
    plt.suptitle(kwargs['the_sup_title']['label'],
                 fontdict=kwargs['sup_title_style'],
                 color=kwargs['the_sup_title']['color'],
                 x=kwargs['sup_title_position']['x']
                )

    handles, labels = ax.get_legend_handles_labels()
    this = ax.legend(handles[::-1], labels[::-1], **kwargs['the_legend_style'])
    this._legend_box.align = kwargs['legend_title']['align']
    save_the_figure(**kwargs['save_this'])

    plt.show()
    plt.close()
