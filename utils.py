import pandas as pd


def matchByDateAndValue(df1, df1cols, df2, df2cols, timeDelta='10 days', valueDelta=0.1, absolute=False):
    a = df1[df1cols]
    b = df2[df2cols]
    matched = []

    def naive_transaction_matcher(x):
        possible = b.drop(index=matched)
        possibleByDate = (
            possible[df2cols[0]] - x[df1cols[0]]).abs().sort_values(ascending=True)
        possibleByDate = possibleByDate[possibleByDate < pd.Timedelta(
            timeDelta)]
        if len(possibleByDate) == 0:
            return None
        possible = possible.loc[possibleByDate.index]
        possibleValues = possible[df2cols[1]].abs(
        ) if absolute else possible[df2cols[1]]
        targetValue = abs(x[df1cols[1]]) if absolute else x[df1cols[1]]
        possibleByAmount = (
            possibleValues - targetValue).abs().sort_values(ascending=True)
        possibleByAmount = possibleByAmount[possibleByAmount <
                                            possible.loc[possibleByAmount.index][df2cols[1]] * valueDelta]
        if len(possibleByAmount) == 0:
            return None
        id = int(possibleByAmount.index[0])
        matched.append(id)
        return id
    indexes = pd.DataFrame(a.apply(
        naive_transaction_matcher, axis=1).dropna().astype('int'), columns=["df2key"])
    return df1.join(indexes).join(df2, on="df2key")
