# Classic Rock Data — Phase 4

Search the dataset and compare a song to the average song of each decade.

```bash
python -m pip install -r requirements.txt
python main.py
```

Enter a full or partial title. If there is no exact or partial match, similar spellings are suggested. Select the intended artist, album, and year from the results.

The program standardizes nine audio features using the overall dataset mean and standard deviation, calculates the mean of each feature per decade, and ranks decades by Euclidean distance. All available songs are included in the averages; missing values are ignored for each feature. The selected song must have all usable features. Features with no usable standard deviation are omitted. Key, mode, and time signature are excluded because they need different treatment. The scores are distances, not probabilities. This is an exploratory comparison: the selected song contributes to its own decade's average, so the result is not an independent evaluation of prediction accuracy.
