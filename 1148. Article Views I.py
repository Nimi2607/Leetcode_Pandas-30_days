import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    unique_val = sorted(views.loc[views['author_id'] == views['viewer_id'], 'author_id'].unique())
    res = pd.DataFrame({'id': unique_val})
    return res
    
    
