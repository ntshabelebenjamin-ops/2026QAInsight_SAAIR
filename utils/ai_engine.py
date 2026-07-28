def analyse_modules(df):

    lowest = df.loc[df["PassRate"].idxmin()]

    return f"""
Module requiring attention:

{lowest['ModuleName']}

Pass Rate: {lowest['PassRate']}%

Average Mark: {lowest['AverageMark']}%

Recommended Actions

• Review assessments

• Strengthen tutoring

• Improve assessment feedback

• Monitor student performance
"""
