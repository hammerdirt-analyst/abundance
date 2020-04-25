from utilities.utility_functions import get_code_totals_from_date_range
from utilities.utility_functions import get_tuples_from_series
from utilities.utility_functions import get_the_rest


def make_stacked_blocks(the_data, ax, color):
    the_bottom = 0
    for i,block in enumerate(the_data):
            if i == 0:
                ax.bar(1, block[1], color=next(color), edgecolor="white", alpha=0.9,
                        label="{}: {:,}".format(block[2],block[1]))
                the_bottom += block[1]
            else:
                ax.bar(1, block[1], color=next(color), edgecolor="white",alpha=0.9,
                       bottom=the_bottom,
                       label="{}: {:,}".format(block[2],block[1]))
                the_bottom += block[1]

def make_blocks(a_df, percent, end_start, total_quant, code_dict, top_ten=False):
    code_totals = get_code_totals_from_date_range(a_df)
    code_totals_tuple = get_tuples_from_series(code_totals)
    code_greater_than = [
        (x[0],x[1],code_dict[x[0]][1])
        for i,x in enumerate(code_totals_tuple)
        if x[1] >= percent
    ]
    the_rest = get_the_rest(code_greater_than, total_quant)
    code_greater_than.append(("Other", the_rest,"*All other objects"))
    return code_greater_than
