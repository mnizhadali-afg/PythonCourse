import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

rolls = [random.randrange(1, 7) for i in range(600)]
values, freqs = np.unique(rolls, return_counts = True)

title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=freqs, palette='bright')
axes.set_title(title)
axes.set(xlabel="Die Value", ylabel="Frequency")

for bar, fr in zip(axes.patches, freqs):
     text_x = bar.get_x() + bar.get_width() / 2.0
     text_y = bar.get_height()
     text = f'{fr:,}\n{fr / len(rolls):.3%}'
     axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
