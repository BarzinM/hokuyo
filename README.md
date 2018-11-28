# Hokuyo

## `Hokuyo` Class

This is a wrapper for `HokuyoLX`.

### `__init__` Method

Constructor of the class.

### `scene` Property

Holds an array of readings. The missed readings are interpolated based on their neighbors.

### `xy` Method

returns x, y values for each reading.

#### Args

- `filter`: If it should filter the missed readings.
- `interpolate`: If it should interpolated the missed readings. If `filter` is set to `True`, then this argument is practically ignored. If `filter=True` and `interpolate=False`, then the missed readings are removed from the returned arrays.

#### Returns

Two 1-D numpy arrays for x and y coordinates.

### `live_plot` Method

Opens a window and continuously plots the readings. This is a blocking function.

#### Args

- `interpolate`: If the missed readings should be interpolated. Similar to `Hokuyo.xy(filter=False, interpolate)`