![LaStrange icon example]( banner.png )

# LaStrange icons

A clean, simple icon theme for easy and focused computing.
Originally developed for [dogfooding](https://en.wikipedia.org/wiki/Eating_your_own_dog_food), the theme aims to be simple in both design and implementation while keeping a distinctly Unix-like aesthetic ...with some modern quality-of-life considerations.

The name is a reference to Tom LaStrange, the inventor of [the TWM window manager](https://en.wikipedia.org/wiki/Twm), which served as the main inspiration for the desktop theme. Other influences include printed paper, [the Athena widget library](https://en.wikipedia.org/wiki/X_Athena_Widgets) and [the Amiga Workbench](https://en.wikipedia.org/wiki/Workbench_(AmigaOS))



# Philosophy

## Do One Thing And Do It Well

This theme being tailor-made for Linux (notably the XFCE desktop environment), it's design is naturally influenced by the Unix philosophy.
Everything is designed according to a set of simple, predefined rules (outlined below), which are to be applied thoroughly, consistently and if possible automatically across the entire system, such that the user's cognitive load is reduced by associative consistency. In short: Things that work similar, look similar, are similar.

## No Frills, No Distractions, No Secrets

Most modern UI designs attempt to simplify the user experience by hiding or obfuscating less important features. Especially in flat designs this tends to lead to confusion about what is interactible, in which way and how the UI is organized.

Beyond that many modern UI designs also employ so called "calls to action". In practice, this usually means that elements the designer deems important are emphasized by making them attention-grabbing, which can be distracting as well as allow for [dark patterns](https://en.wikipedia.org/wiki/Dark_pattern).

LaStrange does not impose any particular order of importance to an action. Instead, everything is presented equally based on it's interactive properties, with the UI relying instead on visual variables such as shape, texture and size, as well as the laws of Gestalt to convey information about the UI. This leads to a clean, consistent and uncluttered experience tailored to users who know what they want their system to do.

## Let The Computer Do The Work

Wherever possible, everything is rendered on-the-fly, **without** the use of any pre-built assets (due to technical restrictions this currently only applies to the GTK theme). This reduces labour effort, keeps consistency and is better scalable to increasing display resolutions/pixel densities. In case of [the LaStrange icon theme](https://github.com/zibonbadi/lastrange-icons/), this means that *everything* will be built upon vector graphics only, whereas [the LaStrange desktop theme](https://github.com/zibonbadi/lastrange-gtk-theme/) solely uses CSS instead.

## You Are Not Alone

Every design exists within a context. Thus, it is not enough for a UI-design to be internally consistent; it has to conform to the UI/UX guidelines of it's context as well to ensure a pleasant, consistent user experience.
For example, [the LaStrange icon theme](https://github.com/zibonbadi/lastrange-icons/) is designed to work within both light and dark modes based on the same set of icons.

# Practice

## Design Rule Cheat Sheet

1. Preserve whitespace.
2. Color signifies interactivity and active selection. More detail on the official color palette in the above section "Color Palette".
3. Texture creates detail. Detail attracts attention. Grabbing attention is bad.
	a. Elements that are supposed to be grabbable (e.g. window borders) are textured using subtle, horizontal stripes.
	b. Disabled/inaccessible elements are textured with thick, diagonal stripes, akin to barrier tape.
4. Keep it flat and two-dimensional. Use the laws of Gestalt to organize things visually. If you need to explicitly separate, do so using lines.
5. Do **not** indicate three-dimensionality through brightness-based methods (e.g. shadows, gradiens, Neumorphism). Instead, use line thickness to give it the appearance of being printed onto paper as if to mimick something lying in front of the viewer on a table.

## Color palette

The aim of of LaStrange lies in simplifying UI visuals by reducing attention-grabbing colors down to a minimum. Thus color is to be used sparingly, with a main highlight color being used to indicate interactivity.
The main shades of light and dark grey have also intentionally been chosen to reduce eye strain due to high contrast on bright displays.

### Primary colors

Although LaStrange is built in such a way that it allows for easy creation of custom color pallettes (a fact which is further highlighted by the included theme set *Default, Dark, Solarized Light, Solarized Dark & Industrial*), the overall design is based on the 3 primary colors listed below:


| Color | dark | light |
|--|--|--|
| Black | |	#1f1f1f	|
| White | |	#d9d9d9	|
| Cyan	|	#19a698 |	#22AA99 (#47ccbf for use in 16 color mode)	|

### Secondary Palette (for 16 colors)

| Color | dark | light |
|--|--|--|
| Red |	#cc3333 |	#ff7373
| Green |	#179917 |	#00de00
| Yellow |	#a6954b |	#cca700
| Blue |	#175ce6 |	#8797ff
| Magenta |	#9a19a6 |	#f066ff

