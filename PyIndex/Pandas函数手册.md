# Pandas 函数手册





| 函数                                             | 说明                                                         |
| ------------------------------------------------ | ------------------------------------------------------------ |
| **输入 / 输出**                                  |                                                              |
| **pickling**                                     |                                                              |
| read_pickle(path[, compression])                 | 从文件中加载 pickled Pandas 对象 (或任何对象)。              |
| **表格**                                         |                                                              |
| read_table(filepath_or_buffer[, sep, …])         | 将通用分隔文件读入 DataFrame                                 |
| read_csv(filepath_or_buffer[, sep, …])           | 将 CSV (逗号分隔) 文件读入 DataFrame                         |
| read_fwf(filepath_or_buffer[, colspecs, widths]) | 将固定宽度格式化行的表读入 DataFrame                         |
| read_msgpack(path_or_buf[, encoding, iterator])  | 从指定的文件路径加载 msgpackPandas 对象                      |
| **剪贴板**                                       |                                                              |
| read_clipboard([sep])                            | 从剪贴板读取文本并传递给 read _ table。                      |
| **EXCEL**                                        |                                                              |
| read_excel(io[, sheet_name, header, names, …])   | 将 Excel 表格读入 PandasDataFrame                            |
| ExcelFile.parse([sheet_name, header, names, …])  | 将指定的工作表解析为 DataFrame                               |
| **JSON**                                         |                                                              |
| read_json([path_or_buf, orient, typ, dtype, …])  | 将 JSON 字符串转换为 Pandas 对象                             |
| json_normalize(data[, record_path, meta, …])     | 将半结构化 JSON 数据 “标准化” 为平面表                       |
| build_table_schema(data[, index, …])             | 根据数据创建表架构。                                         |
| **HTML**                                         |                                                              |
| read_html(io[, match, flavor, header, …])        | 将 HTML 表读入 DataFrame 对象列表。                          |
| **HDFStore : PyTables ( HDF5 )**                 |                                                              |
| read_hdf(path_or_buf[, key, mode])               | 从商店里读，如果我们开了就关门。                             |
| HDFStore.put(key, value[, format, append])       | 将对象存储在 HDFStore 中                                     |
| HDFStore.append(key, value[, format, …])         | 追加到文件中的表中。                                         |
| HDFStore.get(key)                                | 检索文件中存储 Pandas 对象                                   |
| HDFStore.select(key[, where, start, stop, …])    | 检索文件中存储的 Pandas 对象，可选地基于 where 标准          |
| HDFStore.info()                                  | 打印商店的详细信息                                           |
| HDFStore.keys()                                  | 返回与 HDFStore 中存储的对象相对应的键 (可能无序) 列表。     |
| **feather**                                      |                                                              |
| read_feather(path[, nthreads])                   | 从文件路径加载羽化格式的对象                                 |
| **Parquet**                                      |                                                              |
| read_parquet(path[, engine, columns])            | 从文件路径加载 parquet 对象，返回 DataFrame。                |
| **SAS**                                          |                                                              |
| read_sas(filepath_or_buffer[, format, …])        | 读取存储为 XPORT 或 SAS7BDAT 格式文件的 SAS 文件。           |
| **SQL**                                          |                                                              |
| read_sql_table(table_name, con[, schema, …])     | 将 SQL 数据库表读入 DataFrame。                              |
| read_sql_query(sql, con[, index_col, …])         | 将 SQL 查询读入 DataFrame。                                  |
| read_sql(sql, con[, index_col, …])               | 将 SQL 查询或数据库表读入 DataFrame。                        |
| **Google BigQuery**                              |                                                              |
| read_gbq(query[, project_id, index_col, …])      | 从 Google BigQuery 加载数据。                                |
| **Stata**                                        |                                                              |
| read_stata(filepath_or_buffer[, …])              | 将 Stata 文件读入 DataFrame。                                |
| StataReader.data(**kwargs)                       | (已弃用) 从 Stata 文件读取观察结果，将其转换为 DataFrame     |
| StataReader.data_label()                         | 返回 Stata 文件的数据标签                                    |
| StataReader.value_labels()                       | 返回 dict，将每个变量名与 dict 相关联，将每个值与其对应的标签相关联 |
| StataReader.variable_labels()                    | 以 dict 形式返回变量标签，将每个变量名称与相应的标签相关联   |
| StataWriter.write_file()                         | -                                                            |

## 一般职能

| 函数                                             | 说明                                                         |
| ------------------------------------------------ | ------------------------------------------------------------ |
| **数据操作**                                     |                                                              |
| melt(frame[, id_vars, value_vars, var_name, …])  | “取消固定” 从宽格式到长格式的 DataFrame，可选地保留标识符变量集。 |
| pivot(index, columns, values)                    | 根据此 DataFrame 的 3 列生成 “pivot” 表。                    |
| pivot_table(data[, values, index, columns, …])   | 创建电子表格样式的透视表作为 DataFrame 架。                  |
| crosstab(index, columns[, values, rownames, …])  | 计算两个 (或更多) 因素的简单交叉列表。                       |
| cut(x, bins[, right, labels, retbins, …])        | 将值绑定到离散间隔中。                                       |
| qcut(x, q[, labels, retbins, precision, …])      | 基于分位数的离散化函数。                                     |
| merge(left, right[, how, on, left_on, …])        | 通过按列或索引执行数据库样式的联接操作来合并 DataFrame 对象。 |
| merge_ordered(left, right[, on, left_on, …])     | 使用为时序数据等有序数据设计的可选填充 / 插值执行合并。      |
| merge_asof(left, right[, on, left_on, …])        | 执行 asof 合并。                                             |
| concat(objs[, axis, join, join_axes, …])         | 沿特定轴连接 Pandas 对象，沿其他轴连接可选的 set 逻辑。      |
| get_dummies(data[, prefix, prefix_sep, …])       | 将分类变量转换为虚拟 / 指示变量                              |
| factorize(values[, sort, order, …])              | 将对象编码为枚举类型或分类变量。                             |
| unique(values)                                   | 基于哈希表的唯一性。                                         |
| wide_to_long(df, stubnames, i, j[, sep, suffix]) | 宽 Panel 到长格式。                                          |
| **顶级缺失数据**                                 |                                                              |
| isna(obj)                                        | 检测阵列状对象的缺失值。                                     |
| isnull(obj)                                      | 检测阵列状对象的缺失值。                                     |
| notna(obj)                                       | 检测阵列状对象的未丢失值。                                   |
| notnull(obj)                                     | 检测阵列状对象的未丢失值。                                   |
| **顶级转换**                                     |                                                              |
| to_numeric(arg[, errors, downcast])              | 将参数转换为数字类型。                                       |
| **顶级处理类日期**                               |                                                              |
| to_datetime(arg[, errors, dayfirst, …])          | 将参数转换为日期时间。                                       |
| to_timedelta(arg[, unit, box, errors])           | 将参数转换为时间增量                                         |
| date_range([start, end, periods, freq, tz, …])   | 返回固定频率的日期时间索引。                                 |
| bdate_range([start, end, periods, freq, tz, …])  | 返回固定频率 DatetimeIndex，默认频率为工作日                 |
| period_range([start, end, periods, freq, name])  | 返回固定频率周期索引，默认频率为 day (日历)                  |
| timedelta_range([start, end, periods, freq, …])  | 返回固定频率 timedeltindex，默认频率为天                     |
| infer_freq(index[, warn])                        | 根据输入索引推断最可能的频率。                               |
| **高层处理间隔**                                 |                                                              |
| interval_range([start, end, periods, freq, …])   | 返回固定频率的 internalindex                                 |
| **顶级评估**                                     |                                                              |
| eval(expr[, parser, engine, truediv, …])         | 使用各种后端将 Python 表达式计算为字符串。                   |
| **测试**                                         |                                                              |
| test([extra_args])                               | -                                                            |

## Series

| 函数                                              | 说明                                                         |              |
| ------------------------------------------------- | ------------------------------------------------------------ | ------------ |
| **构造器**                                        |                                                              |              |
| Series([data, index, dtype, name, copy, …])       | 带有轴标签的一维 ndarray (包括时间 Series)。                 |              |
| **属性**                                          |                                                              |              |
| **轴线**                                          |                                                              |              |
| Series.index                                      | Series 的索引 (轴标签)。                                     |              |
| Series.values                                     | 根据 dtype，返回 ndarray 或类似 ndarray 的 Series            |              |
| Series.dtype                                      | 返回基础数据的 dtype 对象                                    |              |
| Series.ftype                                      | 如果数据稀疏                                                 | 密集，则返回 |
| Series.shape                                      | 返回基础数据形状的元组                                       |              |
| Series.nbytes                                     | 返回基础数据中的字节数                                       |              |
| Series.ndim                                       | 根据定义 1 返回基础数据的维数                                |              |
| Series.size                                       | 返回基础数据中的元素数                                       |              |
| Series.strides                                    | 返回基础数据的步长                                           |              |
| Series.itemsize                                   | 返回基础数据项的 dtype 大小                                  |              |
| Series.base                                       | 如果共享基础数据的内存，则返回基对象                         |              |
| Series.T                                          | 返回转置，这是自我定义                                       |              |
| Series.memory_usage([index, deep])                | 返回 Series 的内存使用情况。                                 |              |
| Series.hasnans                                    | 如果我有 nans 就回来；启用各种性能加速                       |              |
| Series.flags                                      | -                                                            |              |
| Series.empty                                      | -                                                            |              |
| Series.dtypes                                     | 返回基础数据的 dtype 对象                                    |              |
| Series.ftypes                                     | 如果数据稀疏                                                 | 密集，则返回 |
| Series.data                                       | 返回基础数据的数据指针                                       |              |
| Series.is_copy                                    | -                                                            |              |
| Series.name                                       | -                                                            |              |
| Series.put(*args, **kwargs)                       | 如果 put 方法有值属性，则将其应用于该属性。                  |              |
| **转变**                                          |                                                              |              |
| Series.astype(dtype[, copy, errors])              | 将 Pandas 对象转换为指定的 dtype dtype。                     |              |
| Series.infer_objects()                            | 尝试为对象列推断更好的数据类型。                             |              |
| Series.convert_objects([convert_dates, …])        | (已弃用) 尝试推断对象列的更好 dtype。                        |              |
| Series.copy([deep])                               | 复制此对象的索引和数据。                                     |              |
| Series.bool()                                     | 返回单个元素 PandasObject 的布尔。                           |              |
| Series.to_period([freq, copy])                    | 以所需频率将 Series 从 DatetimeIndex 转换为周期索引 (如果未通过，则从索引推断) |              |
| Series.to_timestamp([freq, how, copy])            | 转换为时间段开始时时间戳的日期时间索引                       |              |
| Series.tolist()                                   | 返回值列表。                                                 |              |
| Series.get_values()                               | 与值相同 (但处理稀疏转换)；是一种观点                        |              |
| **索引、迭代**                                    |                                                              |              |
| Series.get(key[, default])                        | 从给定键 (DataFrame 列、Panel 切片等) 的对象中获取项目。) .  |              |
| Series.at                                         | 访问行 / 列标签对的单个值。                                  |              |
| Series.iat                                        | 按整数位置访问行 / 列对的单个值。                            |              |
| Series.loc                                        | 通过标签或布尔数组访问一组行和列。                           |              |
| Series.iloc                                       | 用于按位置选择的纯整数位置索引。                             |              |
| Series.**iter**()                                 | 返回值的迭代器。                                             |              |
| Series.iteritems()                                | 懒洋洋地迭代 (索引，值) 元组                                 |              |
| Series.items()                                    | 懒洋洋地迭代 (索引，值) 元组                                 |              |
| Series.keys()                                     | 索引别名                                                     |              |
| Series.pop(item)                                  | 返回项目并从框架中删除。                                     |              |
| Series.item()                                     | 以 python 标量形式返回基础数据的第一个元素                   |              |
| Series.xs(key[, axis, level, drop_level])         | 从 Series/DataFrame 返回横截面 (行或列)。                    |              |
| **二元算子函数**                                  |                                                              |              |
| Series.add(other[, level, fill_value, axis])      | Series 和其他元素相加 (二进制运算符相加)。                   |              |
| Series.sub(other[, level, fill_value, axis])      | Series 减法和其他元素减法 (二进制运算符 sub)。               |              |
| Series.mul(other[, level, fill_value, axis])      | 级数与其他元素相乘 (二元运算符 mul)。                        |              |
| Series.div(other[, level, fill_value, axis])      | Series 和其他元素的浮动除法 (二元运算符 truediv)。           |              |
| Series.truediv(other[, level, fill_value, axis])  | Series 和其他元素的浮动除法 (二元运算符 truediv)。           |              |
| Series.floordiv(other[, level, fill_value, axis]) | 按元素对 Series 和其他 Series 进行整数除法 (二进制运算符 flooddiv)。 |              |
| Series.mod(other[, level, fill_value, axis])      | Series 模和其他元素方式 (二进制运算符 mod)。                 |              |
| Series.pow(other[, level, fill_value, axis])      | 级数指数幂和其他元素幂 (二元算子幂)。                        |              |
| Series.radd(other[, level, fill_value, axis])     | 级数和其他元素相加 (二元算子 radd)。                         |              |
| Series.rsub(other[, level, fill_value, axis])     | Series 减法和其他元素减法 (二元运算符 rsub)。                |              |
| Series.rmul(other[, level, fill_value, axis])     | 级数与其他元素相乘 (二元运算符 rmul)。                       |              |
| Series.rdiv(other[, level, fill_value, axis])     | Series 和其他元素的浮动划分 (二元运算符 rtruediv)。          |              |
| Series.rtruediv(other[, level, fill_value, axis]) | Series 和其他元素的浮动划分 (二元运算符 rtruediv)。          |              |
| Series.rfloordiv(other[, level, fill_value, …])   | 整数除法 Series 和其他，元素方式 (二元运算符 rfloordiv)。    |              |
| Series.rmod(other[, level, fill_value, axis])     | Series 模和其他元素 (二元运算符 rmod)。                      |              |
| Series.rpow(other[, level, fill_value, axis])     | 级数的指数幂和其他元素的指数幂 (二元算子 rpow)。             |              |
| Series.combine(other, func[, fill_value])         | 当一个 Series 或另一个 Series 中缺少索引时，使用给定函数和可选填充值对两个 Series 执行元素二进制操作 |              |
| Series.combine_first(other)                       | 组合 Series 值，首先选择调用 Series 的值。                   |              |
| Series.round([decimals])                          | 将 Series 中的每个值舍入到给定的小数位数。                   |              |
| Series.lt(other[, level, fill_value, axis])       | 少于 Series 和其他元素 (二元运算符 lt)。                     |              |
| Series.gt(other[, level, fill_value, axis])       | 大于 Series 和其他元素 (二元运算符 gt)。                     |              |
| Series.le(other[, level, fill_value, axis])       | 小于或等于级数和其他元素的 (二元运算符 le)。                 |              |
| Series.ge(other[, level, fill_value, axis])       | 大于或等于 Series 和其他元素的 (二元运算符 ge)。             |              |
| Series.ne(other[, level, fill_value, axis])       | 不等于级数等，按元素计算 (二元运算符 ne)。                   |              |
| Series.eq(other[, level, fill_value, axis])       | 等于级数和其他，按元素计算 (二元运算符 eq)。                 |              |
| Series.product([axis, skipna, level, …])          | 返回请求轴值的乘积                                           |              |
| Series.dot(other)                                 | 与 DataFrame 的矩阵乘法或与 Series 对象的内积。              |              |
| **功能应用程序，GroupBy & windows**               |                                                              |              |
| Series.apply(func[, convert_dtype, args])         | 调用 Series 值上的函数。                                     |              |
| Series.agg(func[, axis])                          | 使用指定轴上的一个或多个操作聚合。                           |              |
| Series.aggregate(func[, axis])                    | 使用指定轴上的一个或多个操作聚合。                           |              |
| Series.transform(func, *args, **kwargs)           | 调用函数生成类似索引的 NDFrame，并返回带有转换值的 NDFrame   |              |
| Series.map(arg[, na_action])                      | 使用输入对应关系映射 Series 值 (dict、Series 或函数)。       |              |
| Series.groupby([by, axis, level, as_index, …])    | 使用映射程序 (dict 或 key 函数，将给定函数应用于组，将结果作为 Series 返回) 或按一 Series 列对 Series 进行分组。 |              |
| Series.rolling(window[, min_periods, …])          | 提供滚动窗口计算。                                           |              |
| Series.expanding([min_periods, center, axis])     | 提供扩展转换。                                               |              |
| Series.ewm([com, span, halflife, alpha, …])       | 提供指数加权函数                                             |              |
| Series.pipe(func, *args, **kwargs)                | 应用 func (自我，* args，* * kwargs)                         |              |
| **计算 / 描述统计**                               |                                                              |              |
| Series.abs()                                      | 返回每个元素具有绝对值的 Series/DataFrame。                  |              |
| Series.all([axis, bool_only, skipna, level])      | 返回 Series 轴或 DataFrame 轴上的所有元素是否为 True。       |              |
| Series.any([axis, bool_only, skipna, level])      | 返回在请求的轴上是否有任何元素为真。                         |              |
| Series.autocorr([lag])                            | 滞后 - N 自相关                                              |              |
| Series.between(left, right[, inclusive])          | 返回等效于左 < = Series < = right 的布尔级数。               |              |
| Series.clip([lower, upper, axis, inplace])        | 输入阈值处的修剪值。                                         |              |
| Series.clip_lower(threshold[, axis, inplace])     | 返回值低于阈值的输入副本被截断。                             |              |
| Series.clip_upper(threshold[, axis, inplace])     | 返回截断值大于给定值的输入副本。                             |              |
| Series.corr(other[, method, min_periods])         | 计算与其他 Series 的相关性，不包括缺失值                     |              |
| Series.count([level])                             | Series 中非 NA /null 观测值的返回数                          |              |
| Series.cov(other[, min_periods])                  | 用 Series 计算协方差，不包括缺失值                           |              |
| Series.cummax([axis, skipna])                     | 返回 DataFrame 或 Series 轴上的累积最大值。                  |              |
| Series.cummin([axis, skipna])                     | 返回 DataFrame 或 Series 轴上的累积最小值。                  |              |
| Series.cumprod([axis, skipna])                    | 通过 DataFrame 或 Series 轴返回累积产品。                    |              |
| Series.cumsum([axis, skipna])                     | 返回 DataFrame 或 Series 轴上的累计总和。                    |              |
| Series.describe([percentiles, include, exclude])  | 生成描述性统计数据，总结数据集分布的中心趋势、分散和形状，不包括 NaN 值。 |              |
| Series.diff([periods])                            | 元素的第一离散差。                                           |              |
| Series.factorize([sort, na_sentinel])             | 将对象编码为枚举类型或分类变量。                             |              |
| Series.kurt([axis, skipna, level, numeric_only])  | 使用 Fisher 的峰度定义返回请求轴上的无偏峰度 (正常峰度 = = 0.0)。 |              |
| Series.mad([axis, skipna, level])                 | 返回请求轴值的平均绝对偏差                                   |              |
| Series.max([axis, skipna, level, numeric_only])   | 此方法返回对象中值的最大值。                                 |              |
| Series.mean([axis, skipna, level, numeric_only])  | 返回请求轴值的平均值                                         |              |
| Series.median([axis, skipna, level, …])           | 返回请求轴的值的中间值                                       |              |
| Series.min([axis, skipna, level, numeric_only])   | 此方法返回对象中值的最小值。                                 |              |
| Series.mode()                                     | 返回数据集的模式。                                           |              |
| Series.nlargest([n, keep])                        | 返回最大的 n 个元素。                                        |              |
| Series.nsmallest([n, keep])                       | 返回最小的 n 个元素。                                        |              |
| Series.pct_change([periods, fill_method, …])      | 当前元素和先前元素之间的百分比变化。                         |              |
| Series.prod([axis, skipna, level, …])             | 返回请求轴值的乘积                                           |              |
| Series.quantile([q, interpolation])               | 给定分位数的返回值，即 la 数值百分位。                       |              |
| Series.rank([axis, method, numeric_only, …])      | 沿轴计算数值数据列 (1 到 n)。                                |              |
| Series.sem([axis, skipna, level, ddof, …])        | 返回请求轴上平均值的无偏标准误差。                           |              |
| Series.skew([axis, skipna, level, numeric_only])  | 返回由 N - 1 归一化的请求轴上的无偏歪斜                      |              |
| Series.std([axis, skipna, level, ddof, …])        | 返回要求轴上的样品标准偏差。                                 |              |
| Series.sum([axis, skipna, level, …])              | 返回请求轴的值之和                                           |              |
| Series.var([axis, skipna, level, ddof, …])        | 返回请求轴上的无偏方差。                                     |              |
| Series.kurtosis([axis, skipna, level, …])         | 使用 Fisher 的峰度定义返回请求轴上的无偏峰度 (正常峰度 = = 0.0)。 |              |
| Series.unique()                                   | 返回 Series 对象的唯一值。                                   |              |
| Series.nunique([dropna])                          | 返回对象中唯一元素的数目。                                   |              |
| Series.is_unique                                  | 如果对象中的值是唯一的，则返回 boolean                       |              |
| Series.is_monotonic                               | 如果对象中的值是单调递增的，则返回 boolean                   |              |
| Series.is_monotonic_increasing                    | 如果对象中的值是单调递增的，则返回 boolean                   |              |
| Series.is_monotonic_decreasing                    | 如果对象中的值是单调递减的，则返回 boolean                   |              |
| Series.value_counts([normalize, sort, …])         | 返回包含唯一值计数的对象。                                   |              |
| Series.compound([axis, skipna, level])            | 返回请求轴值的复合百分比                                     |              |
| Series.nonzero()                                  | 返回非零元素的整数索引                                       |              |
| Series.ptp([axis, skipna, level, numeric_only])   | 返回对象中最大值和最小值之间的差值。                         |              |
| **重新设计 / 选择 / 标签操作**                    |                                                              |              |
| Series.align(other[, join, axis, level, …])       | 将轴上的两个对象与每个轴索引的指定连接方法对齐               |              |
| Series.drop([labels, axis, index, columns, …])    | 返回删除了指定索引标签的 Series。                            |              |
| Series.drop_duplicates([keep, inplace])           | 返回删除重复值的 Series。                                    |              |
| Series.duplicated([keep])                         | 指示重复的 Series 值。                                       |              |
| Series.equals(other)                              | 确定两个 NDFrame 对象是否包含相同的元素。                    |              |
| Series.first(offset)                              | 基于日期偏移对时间 Series 数据初始周期进行细分的便捷方法。   |              |
| Series.head([n])                                  | 返回前 n 行。                                                |              |
| Series.idxmax([axis, skipna])                     | 返回最大值的行标签。                                         |              |
| Series.idxmin([axis, skipna])                     | 返回最小值的行标签。                                         |              |
| Series.isin(values)                               | 检查值是否包含在 Series 中。                                 |              |
| Series.last(offset)                               | 基于日期偏移对时间 Series 数据的最终周期进行细分的便捷方法。 |              |
| Series.reindex([index])                           | 用可选的填充逻辑使 Series 符合新索引，将 NA / NaN 放置在前一个索引中没有值的位置。 |              |
| Series.reindex_like(other[, method, copy, …])     | 将具有匹配索引的对象返回给我自己。                           |              |
| Series.rename([index])                            | 更改 Series 索引标签或名称                                   |              |
| Series.rename_axis(mapper[, axis, copy, inplace]) | 更改索引或列的名称。                                         |              |
| Series.reset_index([level, drop, name, inplace])  | 使用索引重置生成新的 DataFrame 或 Series。                   |              |
| Series.sample([n, frac, replace, weights, …])     | 从对象轴返回项目的随机样本。                                 |              |
| Series.select(crit[, axis])                       | (已弃用) 返回与轴标签匹配条件相对应的数据                    |              |
| Series.set_axis(labels[, axis, inplace])          | 为给定轴指定所需的索引。                                     |              |
| Series.take(indices[, axis, convert, is_copy])    | 沿轴返回给定位置索引中的元素。                               |              |
| Series.tail([n])                                  | 返回最后 n 行。                                              |              |
| Series.truncate([before, after, axis, copy])      | 在某个索引值前后截断 Series 或 DataFrame。                   |              |
| Series.where(cond[, other, inplace, axis, …])     | 返回与 self 形状相同的对象，其对应条目来自 self，cond 为 True，否则来自其他。 |              |
| Series.mask(cond[, other, inplace, axis, …])      | 返回与 self 形状相同的对象，其对应条目来自 self，cond 为 False，否则来自其他。 |              |
| Series.add_prefix(prefix)                         | 带字符串前缀的前缀标签。                                     |              |
| Series.add_suffix(suffix)                         | 带有字符串后缀的后缀标签。                                   |              |
| Series.filter([items, like, regex, axis])         | 根据指定索引中的标签子集 DataFrame 的行或列。                |              |
| **缺失数据处理**                                  |                                                              |              |
| Series.isna()                                     | 检测缺失值。                                                 |              |
| Series.notna()                                    | 检测现有 (未丢失) 值。                                       |              |
| Series.dropna([axis, inplace])                    | 返回删除了缺少值的新 Series。                                |              |
| Series.fillna([value, method, axis, …])           | 使用指定的方法填写 NA / NaN 值                               |              |
| Series.interpolate([method, axis, limit, …])      | 根据不同的方法插值。                                         |              |
| **整形、分选**                                    |                                                              |              |
| Series.argsort([axis, kind, order])               | 覆盖 ndarray . argsort。                                     |              |
| Series.argmin([axis, skipna])                     | (已弃用)..                                                   |              |
| Series.argmax([axis, skipna])                     | (已弃用)..                                                   |              |
| Series.reorder_levels(order)                      | 使用输入顺序重新排列索引级别。                               |              |
| Series.sort_values([axis, ascending, …])          | 按值排序。                                                   |              |
| Series.sort_index([axis, level, ascending, …])    | 按索引标签排序 Series。                                      |              |
| Series.swaplevel([i, j, copy])                    | 交换多索引中的级别 I 和 j                                    |              |
| Series.unstack([level, fill_value])               | 史黛克，又名                                                 |              |
| Series.searchsorted(value[, side, sorter])        | 查找应该插入元素以维持秩序的索引。                           |              |
| Series.ravel([order])                             | 将展平的基础数据作为 ndarray 返回                            |              |
| Series.repeat(repeats, *args, **kwargs)           | 重复 Series 的元素。                                         |              |
| Series.squeeze([axis])                            | 挤压长度 1 尺寸。                                            |              |
| Series.view([dtype])                              | 创建 Series 的新视图。                                       |              |
| Series.sortlevel([level, ascending, …])           | (已弃用) 按选定级别对具有多索引的 Series 进行排序。          |              |
| **合并 / 加入 / 合并**                            |                                                              |              |
| Series.append(to_append[, ignore_index, …])       | 连接两个或多个 Series。                                      |              |
| Series.replace([to_replace, value, inplace, …])   | 将 to _ replace 中给定的值替换为值。                         |              |
| Series.update(other)                              | 使用传递 Series 中的非 NA 值就地修改 Series。                |              |
| **时间 Series 相关的**                            |                                                              |              |
| Series.asfreq(freq[, method, how, …])             | 将时间 Series 转换为指定频率。                               |              |
| Series.asof(where[, subset])                      | 取不带 NaN 的最后一行 (或者在 DataFrame 的情况下，不带 NaN 的最后一行仅考虑列的子集) |              |
| Series.shift([periods, freq, axis])               | 按所需周期数移位索引，可选时间频率                           |              |
| Series.first_valid_index()                        | 返回第一个非 NA /null 值的索引。                             |              |
| Series.last_valid_index()                         | 返回最后一个非 NA /null 值的索引。                           |              |
| Series.resample(rule[, how, axis, …])             | 时间 Series 频率转换和 Resampling 的便捷方法。               |              |
| Series.tz_convert(tz[, axis, level, copy])        | 将 tz 感知轴转换为目标时区。                                 |              |
| Series.tz_localize(tz[, axis, level, copy, …])    | 将 tz - naive 时间 Series 本地化为目标时区。                 |              |
| Series.at_time(time[, asof])                      | 选择一天中特定时间的值 (例如                                 |              |
| Series.between_time(start_time, end_time[, …])    | 选择一天中特定时间之间的值 (例如，上午 9 : 00 - 9 : 30)。    |              |
| Series.tshift([periods, freq, axis])              | 移动时间索引，使用索引的频率 (如果可用)。                    |              |
| Series.slice_shift([periods, axis])               | 相当于移位而不复制数据。                                     |              |
| **类日期属性**                                    |                                                              |              |
| **日期时间属性**                                  |                                                              |              |
| Series.dt.date                                    | 返回 python datetime . date 对象的 numpy 数组 (即时间戳中没有时区信息的日期部分)。 |              |
| Series.dt.time                                    | 返回 datetime . time 的 numpy 数组。                         |              |
| Series.dt.year                                    | 日期时间的年份                                               |              |
| Series.dt.month                                   | 1 月 = 1 月，12 月 = 12 月                                   |              |
| Series.dt.day                                     | 日期时间的天数                                               |              |
| Series.dt.hour                                    | 日期时间的小时数                                             |              |
| Series.dt.minute                                  | 日期时间的分钟数                                             |              |
| Series.dt.second                                  | 日期时间的秒数                                               |              |
| Series.dt.microsecond                             | 日期时间的微秒                                               |              |
| Series.dt.nanosecond                              | 日期时间的纳秒                                               |              |
| Series.dt.week                                    | 一年中的第几周                                               |              |
| Series.dt.weekofyear                              | 一年中的第几周                                               |              |
| Series.dt.dayofweek                               | 星期一 = 0，星期日 = 6 的星期几                              |              |
| Series.dt.weekday                                 | 星期一 = 0，星期日 = 6 的星期几                              |              |
| Series.dt.dayofyear                               | 一年中的第几天                                               |              |
| Series.dt.quarter                                 | 日期的季度                                                   |              |
| Series.dt.is_month_start                          | 逻辑指示每月第一天 (由频率定义)                              |              |
| Series.dt.is_month_end                            | 指示日期是否为当月的最后一天。                               |              |
| Series.dt.is_quarter_start                        | 指示日期是否为季度的第一天。                                 |              |
| Series.dt.is_quarter_end                          | 指示日期是否为季度的最后一天。                               |              |
| Series.dt.is_year_start                           | 指出日期是否为一年中的第一天。                               |              |
| Series.dt.is_year_end                             | 指出日期是否为一年中的最后一天。                             |              |
| Series.dt.is_leap_year                            | 如果日期属于闰年，则为布尔指示符。                           |              |
| Series.dt.daysinmonth                             | 当月的天数                                                   |              |
| Series.dt.days_in_month                           | 当月的天数                                                   |              |
| Series.dt.tz                                      | -                                                            |              |
| Series.dt.freq                                    | -                                                            |              |
| **日期时间方法**                                  |                                                              |              |
| Series.dt.to_period(*args, **kwargs)              | 以特定频率转换为周期指数。                                   |              |
| Series.dt.to_pydatetime()                         | 将数据作为本机 Python datetime 对象的数组返回                |              |
| Series.dt.tz_localize(*args, **kwargs)            | 将 tz - naive 日期时间索引本地化为 tz 感知的日期时间索引。   |              |
| Series.dt.tz_convert(*args, **kwargs)             | 将 tz 感知的日期时间索引从一个时区转换到另一个时区。         |              |
| Series.dt.normalize(*args, **kwargs)              | 将时间转换为午夜。                                           |              |
| Series.dt.strftime(*args, **kwargs)               | 使用指定的 date _ format 转换为索引。                        |              |
| Series.dt.round(*args, **kwargs)                  | 将数据舍入到指定的频率。                                     |              |
| Series.dt.floor(*args, **kwargs)                  | 将数据降至指定频率。                                         |              |
| Series.dt.ceil(*args, **kwargs)                   | 将数据上限设置为指定频率。                                   |              |
| Series.dt.month_name(*args, **kwargs)             | 返回具有指定区域设置的 DateTimeIndex 的月份名称。            |              |
| Series.dt.day_name(*args, **kwargs)               | 返回具有指定区域设置的 DateTimeIndex 的日期名称。            |              |
| **时间增量属性**                                  |                                                              |              |
| Series.dt.days                                    | 每个元素的天数。                                             |              |
| Series.dt.seconds                                 | 每个元素的秒数 (> = 0 且小于 1 天)。                         |              |
| Series.dt.microseconds                            | 每个元素的微秒数 (> = 0 且小于 1 秒)。                       |              |
| Series.dt.nanoseconds                             | 每个元素的纳秒数 (> = 0 且小于 1 微秒)。                     |              |
| Series.dt.components                              | 返回时间增量组件的 DataFrame (天、小时、分钟、秒、毫秒、微秒、纳秒)。 |              |
| **时间增量法**                                    |                                                              |              |
| Series.dt.to_pytimedelta()                        | 返回本机 datetime . timedelta 对象的数组。                   |              |
| Series.dt.total_seconds(*args, **kwargs)          | 返回每个元素的总持续时间 (以秒为单位)。                      |              |

## 字符串处理

| 函数                                           | 说明                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| Series.str.capitalize()                        | 将 Series / 索引中的字符串转换为大写。                       |
| Series.str.cat([others, sep, na_rep, join])    | 使用给定的分隔符连接 Series / 索引中的字符串。               |
| Series.str.center(width[, fillchar])           | 用附加字符填充 Series / 索引中字符串的左侧和右侧。           |
| Series.str.contains(pat[, case, flags, na, …]) | 测试模式或正则表达式是否包含在 Series 或索引的字符串中。     |
| Series.str.count(pat[, flags])                 | 统计 Series / 索引的每个字符串中模式的出现次数。             |
| Series.str.decode(encoding[, errors])          | 使用指示的编码解码 Series / 索引中的字符串。                 |
| Series.str.encode(encoding[, errors])          | 使用指定的编码对 Series / 索引中的字符串进行编码。           |
| Series.str.endswith(pat[, na])                 | 测试每个字符串元素的结尾是否与模式匹配。                     |
| Series.str.extract(pat[, flags, expand])       | 对于 Series 中的每个主题字符串，从正则表达式 pat 的第一个匹配项中提取组。 |
| Series.str.extractall(pat[, flags])            | 对于 Series 中的每个主题字符串，从正则表达式 pat 的所有匹配项中提取组。 |
| Series.str.find(sub[, start, end])             | 返回 Series / 索引中每个字符串的最低索引，其中子字符串完全包含在 [ start : end 之间。 |
| Series.str.findall(pat[, flags])               | 查找 Series / 索引中所有出现的模式或正则表达式。             |
| Series.str.get(i)                              | 在指定位置从每个组件中提取元素。                             |
| Series.str.index(sub[, start, end])            | 返回 [ start : end 之间子字符串完全包含的每个字符串中的最低索引。 |
| Series.str.join(sep)                           | 作为元素包含在 Series / 索引中的联接列表，带有传递的分隔符。 |
| Series.str.len()                               | 计算 Series / 索引中每个字符串的长度。                       |
| Series.str.ljust(width[, fillchar])            | 在 Series / 索引中字符串的右侧添加一个字符。                 |
| Series.str.lower()                             | 将 Series / 索引中的字符串转换为小写。                       |
| Series.str.lstrip([to_strip])                  | 从左侧删除 Series / 索引中每个字符串的空白 (包括换行符)。    |
| Series.str.match(pat[, case, flags, na, …])    | 确定每个字符串是否与正则表达式匹配。                         |
| Series.str.normalize(form)                     | 返回 Series / 索引中字符串的 Unicode 标准格式。              |
| Series.str.pad(width[, side, fillchar])        | 在 Series / 索引中填充字符串，并在指定侧添加一个字符。       |
| Series.str.partition([pat, expand])            | 在 sep 第一次出现时拆分字符串，返回包含分隔符前部分、分隔符本身和分隔符后部分的 3 个元素。 |
| Series.str.repeat(repeats)                     | 按指示的次数复制 Series / 索引中的每个字符串。               |
| Series.str.replace(pat, repl[, n, case, …])    | 用其他字符串替换 Series / 索引中出现的模式 / 正则表达式。    |
| Series.str.rfind(sub[, start, end])            | 返回 Series / 索引中每个字符串的最高索引，其中子字符串完全包含在 [ start : end 之间。 |
| Series.str.rindex(sub[, start, end])           | 返回 [ start : end 之间子字符串完全包含的每个字符串中的最高索引。 |
| Series.str.rjust(width[, fillchar])            | 用附加字符填充 Series / 索引中字符串的左侧。                 |
| Series.str.rpartition([pat, expand])           | 在 sep 的最后一次出现时拆分字符串，返回包含分隔符前的部分、分隔符本身和分隔符后的部分的 3 个元素。 |
| Series.str.rstrip([to_strip])                  | 从右侧删除 Series / 索引中每个字符串的空白 (包括换行符)。    |
| Series.str.slice([start, stop, step])          | 将 Series / 索引中每个元素的子字符串切片                     |
| Series.str.slice_replace([start, stop, repl])  | 用另一个值替换字符串的位置切片。                             |
| Series.str.split([pat, n, expand])             | 在给定分隔符 / 分隔符周围拆分字符串。                        |
| Series.str.rsplit([pat, n, expand])            | 按给定的分隔符字符串拆分 Series / 索引中的每个字符串，从字符串的末尾开始，一直到前面。 |
| Series.str.startswith(pat[, na])               | 测试每个字符串元素的开头是否与模式匹配。                     |
| Series.str.strip([to_strip])                   | 从 Series / 索引中的每个字符串的左侧和右侧去掉空白 (包括换行符)。 |
| Series.str.swapcase()                          | 转换 Series / 索引中的字符串以进行交换。                     |
| Series.str.title()                             | 将 Series / 索引中的字符串转换为标题大小写。                 |
| Series.str.translate(table[, deletechars])     | 通过给定的映射表映射字符串中的所有字符。                     |
| Series.str.upper()                             | 将 Series / 索引中的字符串转换为大写。                       |
| Series.str.wrap(width, **kwargs)               | 将 Series / 索引中的长字符串包装成长度小于给定宽度的段落。   |
| Series.str.zfill(width)                        | 用 0 填充 Series / 索引中字符串的左侧。                      |
| Series.str.isalnum()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是字母数字。 |
| Series.str.isalpha()                           | 检查 Series / 索引中每个字符串中的所有字符是否为字母。       |
| Series.str.isdigit()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是数字。     |
| Series.str.isspace()                           | 检查 Series / 索引中每个字符串中的所有字符是否为空白。       |
| Series.str.islower()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是小写的。   |
| Series.str.isupper()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是大写的。   |
| Series.str.istitle()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是标题大小写。 |
| Series.str.isnumeric()                         | 检查 Series / 索引中每个字符串中的所有字符是否都是数字。     |
| Series.str.isdecimal()                         | 检查 Series / 索引中每个字符串中的所有字符是否都是十进制的。 |
| Series.str.get_dummies([sep])                  | 按 sep 拆分 Series 中的每个字符串，并返回一帧虚拟 / 指示器变量。 |

series . str 可用于以字符串形式访问 Series 的值，并对其应用多种方法。这些可以像 series . str . <函数 / 属性> 一样访问。

| 函数                                           | 说明                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| Series.str.capitalize()                        | 将 Series / 索引中的字符串转换为大写。                       |
| Series.str.cat([others, sep, na_rep, join])    | 使用给定的分隔符连接 Series / 索引中的字符串。               |
| Series.str.center(width[, fillchar])           | 用附加字符填充 Series / 索引中字符串的左侧和右侧。           |
| Series.str.contains(pat[, case, flags, na, …]) | 测试模式或正则表达式是否包含在 Series 或索引的字符串中。     |
| Series.str.count(pat[, flags])                 | 统计 Series / 索引的每个字符串中模式的出现次数。             |
| Series.str.decode(encoding[, errors])          | 使用指示的编码解码 Series / 索引中的字符串。                 |
| Series.str.encode(encoding[, errors])          | 使用指定的编码对 Series / 索引中的字符串进行编码。           |
| Series.str.endswith(pat[, na])                 | 测试每个字符串元素的结尾是否与模式匹配。                     |
| Series.str.extract(pat[, flags, expand])       | 对于 Series 中的每个主题字符串，从正则表达式 pat 的第一个匹配项中提取组。 |
| Series.str.extractall(pat[, flags])            | 对于 Series 中的每个主题字符串，从正则表达式 pat 的所有匹配项中提取组。 |
| Series.str.find(sub[, start, end])             | 返回 Series / 索引中每个字符串的最低索引，其中子字符串完全包含在 [ start : end 之间。 |
| Series.str.findall(pat[, flags])               | 查找 Series / 索引中所有出现的模式或正则表达式。             |
| Series.str.get(i)                              | 在指定位置从每个组件中提取元素。                             |
| Series.str.index(sub[, start, end])            | 返回 [ start : end 之间子字符串完全包含的每个字符串中的最低索引。 |
| Series.str.join(sep)                           | 作为元素包含在 Series / 索引中的联接列表，带有传递的分隔符。 |
| Series.str.len()                               | 计算 Series / 索引中每个字符串的长度。                       |
| Series.str.ljust(width[, fillchar])            | 在 Series / 索引中字符串的右侧添加一个字符。                 |
| Series.str.lower()                             | 将 Series / 索引中的字符串转换为小写。                       |
| Series.str.lstrip([to_strip])                  | 从左侧删除 Series / 索引中每个字符串的空白 (包括换行符)。    |
| Series.str.match(pat[, case, flags, na, …])    | 确定每个字符串是否与正则表达式匹配。                         |
| Series.str.normalize(form)                     | 返回 Series / 索引中字符串的 Unicode 标准格式。              |
| Series.str.pad(width[, side, fillchar])        | 在 Series / 索引中填充字符串，并在指定侧添加一个字符。       |
| Series.str.partition([pat, expand])            | 在 sep 第一次出现时拆分字符串，返回包含分隔符前部分、分隔符本身和分隔符后部分的 3 个元素。 |
| Series.str.repeat(repeats)                     | 按指示的次数复制 Series / 索引中的每个字符串。               |
| Series.str.replace(pat, repl[, n, case, …])    | 用其他字符串替换 Series / 索引中出现的模式 / 正则表达式。    |
| Series.str.rfind(sub[, start, end])            | 返回 Series / 索引中每个字符串的最高索引，其中子字符串完全包含在 [ start : end 之间。 |
| Series.str.rindex(sub[, start, end])           | 返回 [ start : end 之间子字符串完全包含的每个字符串中的最高索引。 |
| Series.str.rjust(width[, fillchar])            | 用附加字符填充 Series / 索引中字符串的左侧。                 |
| Series.str.rpartition([pat, expand])           | 在 sep 的最后一次出现时拆分字符串，返回包含分隔符前的部分、分隔符本身和分隔符后的部分的 3 个元素。 |
| Series.str.rstrip([to_strip])                  | 从右侧删除 Series / 索引中每个字符串的空白 (包括换行符)。    |
| Series.str.slice([start, stop, step])          | 将 Series / 索引中每个元素的子字符串切片                     |
| Series.str.slice_replace([start, stop, repl])  | 用另一个值替换字符串的位置切片。                             |
| Series.str.split([pat, n, expand])             | 在给定分隔符 / 分隔符周围拆分字符串。                        |
| Series.str.rsplit([pat, n, expand])            | 按给定的分隔符字符串拆分 Series / 索引中的每个字符串，从字符串的末尾开始，一直到前面。 |
| Series.str.startswith(pat[, na])               | 测试每个字符串元素的开头是否与模式匹配。                     |
| Series.str.strip([to_strip])                   | 从 Series / 索引中的每个字符串的左侧和右侧去掉空白 (包括换行符)。 |
| Series.str.swapcase()                          | 转换 Series / 索引中的字符串以进行交换。                     |
| Series.str.title()                             | 将 Series / 索引中的字符串转换为标题大小写。                 |
| Series.str.translate(table[, deletechars])     | 通过给定的映射表映射字符串中的所有字符。                     |
| Series.str.upper()                             | 将 Series / 索引中的字符串转换为大写。                       |
| Series.str.wrap(width, **kwargs)               | 将 Series / 索引中的长字符串包装成长度小于给定宽度的段落。   |
| Series.str.zfill(width)                        | 用 0 填充 Series / 索引中字符串的左侧。                      |
| Series.str.isalnum()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是字母数字。 |
| Series.str.isalpha()                           | 检查 Series / 索引中每个字符串中的所有字符是否为字母。       |
| Series.str.isdigit()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是数字。     |
| Series.str.isspace()                           | 检查 Series / 索引中每个字符串中的所有字符是否为空白。       |
| Series.str.islower()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是小写的。   |
| Series.str.isupper()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是大写的。   |
| Series.str.istitle()                           | 检查 Series / 索引中每个字符串中的所有字符是否都是标题大小写。 |
| Series.str.isnumeric()                         | 检查 Series / 索引中每个字符串中的所有字符是否都是数字。     |
| Series.str.isdecimal()                         | 检查 Series / 索引中每个字符串中的所有字符是否都是十进制的。 |
| Series.str.get_dummies([sep])                  | 按 sep 拆分 Series 中的每个字符串，并返回一帧虚拟 / 指示器变量。 |

## 分类

| 函数                                                         | 说明                                         |
| ------------------------------------------------------------ | -------------------------------------------- |
| **Pandas 定义自定义数据类型，用于表示只能接受有限的固定值集的数据。类别的 dtype 可以由 pandas.api.types.CategoricalDtype 得到** |                                              |
| api.types.CategoricalDtype([categories, ordered])            | 具有类别和有序性的分类数据类型               |
| api.types.CategoricalDtype.categories                        | 包含允许的唯一类别的索引。                   |
| api.types.CategoricalDtype.ordered                           | 类别是否有有序关系                           |
| **类型可以 pandas.Categorical 得到**                         |                                              |
| Categorical(values[, categories, ordered, …])                | 代表经典 R / S + 样式中的分类变量            |
| **当您已经有类别和整数代码时，可以使用 alternational . from _ code ( ) 构造函数:** |                                              |
| Categorical.from_codes(codes, categories[, …])               | 从代码和类别数组中创建类别类型。             |
| **dtype 信息可从分类中获得**                                 |                                              |
| Categorical.dtype                                            | 此实例的类别类型                             |
| Categorical.categories                                       | 这个范畴。                                   |
| Categorical.ordered                                          | 类别是否有有序关系                           |
| Categorical.codes                                            | 此类别的类别代码。                           |
| **NP . asarray (分类) 通过实现数组接口工作。请注意，这将类别转换回 NumPy 数组，因此不会保留类别和顺序信息！** |                                              |
| Categorical.**array**([dtype])                               | numpy 数组接口。                             |
| **类别可以存储在 Series 或 DataFrame 中。要创建一 Seriesdtype 类别，请使用 cat = s . astype (dtype) 或 Series (...，dtype = dtype )，其中 dtype 为** |                                              |
| **字符串 “类别”**                                            |                                              |
| **类别类型的实例。**                                         |                                              |
| **如果该 Series 属于 dtype CategoricalDtype，则可以使用 Series . cat 更改分类数据。此访问器类似于 series . dt 或 series . str，具有以下可用的方法和属性:** |                                              |
| Series.cat.categories                                        | 这个范畴。                                   |
| Series.cat.ordered                                           | 类别是否有有序关系                           |
| Series.cat.codes                                             | -                                            |
| Series.cat.rename_categories(*args, **kwargs)                | 重命名类别。                                 |
| Series.cat.reorder_categories(*args, **kwargs)               | 按照 new _ categories 中的指定重新排序类别。 |
| Series.cat.add_categories(*args, **kwargs)                   | 添加新类别。                                 |
| Series.cat.remove_categories(*args, **kwargs)                | 删除指定的类别。                             |
| Series.cat.remove_unused_categories(*args, …)                | 删除未使用的类别。                           |
| Series.cat.set_categories(*args, **kwargs)                   | 将类别设置为指定的 new _ categories。        |
| Series.cat.as_ordered(*args, **kwargs)                       | 设置要排序的分类                             |
| Series.cat.as_unordered(*args, **kwargs)                     | 将分类设置为无序                             |

## 绘图

| 函数                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **series . plot 是表单 Series 特定绘图方法的可调用方法和命名空间属性。** |                                                              |
| Series.plot([kind, ax, figsize, ….])                         | Series 绘图存取器及方法                                      |
| Series.plot.area(**kwds)                                     | 面积图                                                       |
| Series.plot.bar(**kwds)                                      | 竖线图                                                       |
| Series.plot.barh(**kwds)                                     | 水平柱状图                                                   |
| Series.plot.box(**kwds)                                      | 箱线图                                                       |
| Series.plot.density([bw_method, ind])                        | 使用高斯核生成核密度估计图。                                 |
| Series.plot.hist([bins])                                     | 柱状图                                                       |
| Series.plot.kde([bw_method, ind])                            | 使用高斯核生成核密度估计图。                                 |
| Series.plot.line(**kwds)                                     | 线图                                                         |
| Series.plot.pie(**kwds)                                      | 圆形分格统计图表                                             |
| Series.hist([by, ax, grid, xlabelsize, …])                   | 用 matplotlib 绘制输入 Series 直方图                         |
| **Series 化 / 输入输出 / 转换**                              |                                                              |
| Series.to_pickle(path[, compression, protocol])              | 将对象保存 (Series 化) 到文件中。                            |
| Series.to_csv([path, index, sep, na_rep, …])                 | 将 Series 写入逗号分隔值 (CSV) 文件                          |
| Series.to_dict([into])                                       | 将 Series 转换为 {label - -> value } dict 或 dict 类对象。   |
| Series.to_excel(excel_writer[, sheet_name, …])               | 将 Series 写入 excel 工作表                                  |
| Series.to_frame([name])                                      | 将 Series 转换为 DataFrame                                   |
| Series.to_xarray()                                           | 从 Pandas 对象返回 xarray 对象。                             |
| Series.to_hdf(path_or_buf, key, **kwargs)                    | 使用 HDFStore 将包含的数据写入 HDF5 文件。                   |
| Series.to_sql(name, con[, schema, …])                        | 将存储在 DataFrame 中的记录写入 SQL 数据库。                 |
| Series.to_msgpack([path_or_buf, encoding])                   | msgpack (Series 化) 对象到输入文件路径                       |
| Series.to_json([path_or_buf, orient, …])                     | 将对象转换为 JSON 字符串。                                   |
| Series.to_sparse([kind, fill_value])                         | 将 Series 转换为稀疏 Series                                  |
| Series.to_dense()                                            | 返回 NDFrame 的密集表示 (相对于稀疏)                         |
| Series.to_string([buf, na_rep, …])                           | 呈现 Series 的字符串表示形式                                 |
| Series.to_clipboard([excel, sep])                            | 将对象复制到系统剪贴板。                                     |
| Series.to_latex([buf, columns, col_space, …])                | 将对象呈现为表格环境表。                                     |
| **稀少的**                                                   |                                                              |
| SparseSeries.to_coo([row_levels, …])                         | 从具有多索引的稀疏库中创建一个 scipy . sparse . COO _ matrix。 |
| SparseSeries.from_coo(A[, dense_index])                      | 从一个冷而稀疏的. COO _ matrix 创建一个稀疏的 sereseries。   |

## DataFrame

| 函数                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **构造器**                                                   |                                                              |
| DataFrame([data, index, columns, dtype, copy])               | 二维大小可变的、具有标记轴 (行和列) 的潜在异构表格数据结构。 |
| **属性和基础数据**                                           |                                                              |
| **轴线**                                                     |                                                              |
| DataFrame.index                                              | DataFrame 的索引 (行标签)。                                  |
| DataFrame.columns                                            | DataFrame 的列标签。                                         |
| DataFrame.dtypes                                             | 返回 DataFrame 中的数据类型。                                |
| DataFrame.ftypes                                             | 返回 DataFrame 中的 ftype (稀疏 / 密集和 dtype 的指示)。     |
| DataFrame.get_dtype_counts()                                 | 返回此对象中唯一 dtypes 的计数。                             |
| DataFrame.get_ftype_counts()                                 | (已弃用) 返回此对象中唯一 ftypes 的计数。                    |
| DataFrame.select_dtypes([include, exclude])                  | 根据列 dtypes 返回 DataFrame 列的子集。                      |
| DataFrame.values                                             | 返回 DataFrame 的 Numpy 表示形式。                           |
| DataFrame.get_values()                                       | 将稀疏值转换为密集值后返回 ndarray。                         |
| DataFrame.axes                                               | 返回表示 DataFrame 轴的列表。                                |
| DataFrame.ndim                                               | 返回一个表示轴 / 数组维数的 int。                            |
| DataFrame.size                                               | 返回一个 int，表示此对象中的元素数。                         |
| DataFrame.shape                                              | 返回表示 DataFrame 维度的元组。                              |
| DataFrame.memory_usage([index, deep])                        | 以字节为单位返回每列的内存使用情况。                         |
| DataFrame.empty                                              | 指示 DataFrame 是否为空。                                    |
| DataFrame.is_copy                                            | -                                                            |
| **转变**                                                     |                                                              |
| DataFrame.astype(dtype[, copy, errors])                      | 将 Pandas 对象转换为指定的 dtype dtype。                     |
| DataFrame.convert_objects([convert_dates, …])                | (已弃用) 尝试推断对象列的更好 dtype。                        |
| DataFrame.infer_objects()                                    | 尝试为对象列推断更好的数据类型。                             |
| DataFrame.copy([deep])                                       | 复制此对象的索引和数据。                                     |
| DataFrame.isna()                                             | 检测缺失值。                                                 |
| DataFrame.notna()                                            | 检测现有 (未丢失) 值。                                       |
| DataFrame.bool()                                             | 返回单个元素 PandasObject 的布尔。                           |
| **索引、迭代**                                               |                                                              |
| DataFrame.head([n])                                          | 返回前 n 行。                                                |
| DataFrame.at                                                 | 访问行 / 列标签对的单个值。                                  |
| DataFrame.iat                                                | 按整数位置访问行 / 列对的单个值。                            |
| DataFrame.loc                                                | 通过标签或布尔数组访问一组行和列。                           |
| DataFrame.iloc                                               | 用于按位置选择的纯整数位置索引。                             |
| DataFrame.insert(loc, column, value[, …])                    | 在指定位置将列插入 DataFrame。                               |
| DataFrame.insert(loc, column, value[, …])                    | 在指定位置将列插入 DataFrame。                               |
| DataFrame.**iter**()                                         | 迭代信息轴                                                   |
| DataFrame.items()                                            | 迭代器 (列名，Series) 对。                                   |
| DataFrame.keys()                                             | 获取 “信息轴”(有关详细信息，请参阅索引)                      |
| DataFrame.iteritems()                                        | 迭代器 (列名，Series) 对。                                   |
| DataFrame.iterrows()                                         | 以 (索引、Series) 对形式迭代 DataFrame 行。                  |
| DataFrame.itertuples([index, name])                          | 以 namedtpulles 形式迭代 DataFrame 行，索引值作为元组的第一个元素。 |
| DataFrame.lookup(row_labels, col_labels)                     | 基于标签的 DataFrame “花式索引” 功能。                       |
| DataFrame.pop(item)                                          | 返回项目并从框架中删除。                                     |
| DataFrame.tail([n])                                          | 返回最后 n 行。                                              |
| DataFrame.xs(key[, axis, level, drop_level])                 | 从 Series/DataFrame 返回横截面 (行或列)。                    |
| DataFrame.get(key[, default])                                | 从给定键 (DataFrame 列、Panel 切片等) 的对象中获取项目。) .  |
| DataFrame.isin(values)                                       | 返回布尔 DataFrame，显示 DataFrame 中的每个元素是否包含在值中。 |
| DataFrame.where(cond[, other, inplace, …])                   | 返回与 self 形状相同的对象，其对应条目来自 self，cond 为 True，否则来自其他。 |
| DataFrame.mask(cond[, other, inplace, axis, …])              | 返回与 self 形状相同的对象，其对应条目来自 self，cond 为 False，否则来自其他。 |
| DataFrame.query(expr[, inplace])                             | 使用布尔表达式查询框架的列。                                 |
| **二元算子函数**                                             |                                                              |
| DataFrame.add(other[, axis, level, fill_value])              | 添加 DataFrame 和其他元素 (二进制运算符 add)。               |
| DataFrame.sub(other[, axis, level, fill_value])              | DataFrame 和其他元素相减 (二进制运算符 sub)。                |
| DataFrame.mul(other[, axis, level, fill_value])              | DataFrame 和其他元素的乘法 (二进制运算符 mul)。              |
| DataFrame.div(other[, axis, level, fill_value])              | DataFrame 和其他元素的浮动划分 (二进制运算符 truediv)。      |
| DataFrame.truediv(other[, axis, level, …])                   | DataFrame 和其他元素的浮动划分 (二进制运算符 truediv)。      |
| DataFrame.floordiv(other[, axis, level, …])                  | DataFrame 和其他元素的整数除法 (二进制运算符 flooddiv)。     |
| DataFrame.mod(other[, axis, level, fill_value])              | DataFrame 模和其他元素 (二进制运算符 mod)。                  |
| DataFrame.pow(other[, axis, level, fill_value])              | DataFrame 指数幂和其他元素幂 (二元算子幂)。                  |
| DataFrame.dot(other)                                         | 与 DataFrame 或 Series 对象的矩阵乘法。                      |
| DataFrame.radd(other[, axis, level, fill_value])             | 添加 DataFrame 和其他元素 (二元运算符 radd)。                |
| DataFrame.rsub(other[, axis, level, fill_value])             | DataFrame 和其他元素减法 (二进制运算符 rsub)。               |
| DataFrame.rmul(other[, axis, level, fill_value])             | DataFrame 和其他元素的乘法 (二进制运算符 rmul)。             |
| DataFrame.rdiv(other[, axis, level, fill_value])             | DataFrame 和其他元素的浮动划分 (二进制运算符 rtruediv)。     |
| DataFrame.rtruediv(other[, axis, level, …])                  | DataFrame 和其他元素的浮动划分 (二进制运算符 rtruediv)。     |
| DataFrame.rfloordiv(other[, axis, level, …])                 | DataFrame 和其他元素的整数除法 (二元运算符 rfloordiv)。      |
| DataFrame.rmod(other[, axis, level, fill_value])             | DataFrame 模和其他元素 (二进制运算符 rmod)。                 |
| DataFrame.rpow(other[, axis, level, fill_value])             | DataFrame 和其他元素的指数幂 (二元运算符 rpow)。             |
| DataFrame.lt(other[, axis, level])                           | 灵活比较方法包装                                             |
| DataFrame.gt(other[, axis, level])                           | 灵活比较方法包装器                                           |
| DataFrame.le(other[, axis, level])                           | 灵活比较方法包装                                             |
| DataFrame.ge(other[, axis, level])                           | 灵活比较方法的包装                                           |
| DataFrame.ne(other[, axis, level])                           | 用于灵活比较方法的包装器                                     |
| DataFrame.eq(other[, axis, level])                           | 灵活比较方法包装器                                           |
| DataFrame.combine(other, func[, fill_value, …])              | 添加两个 DataFrame 对象，不传播 NaN 值，因此如果某个 (列，时间) 帧缺少一个值，它将默认为另一帧的值 (也可能是 NaN ) |
| DataFrame.combine_first(other)                               | 组合两个 DataFrame 对象，并在调用方法的帧中默认为非空值。    |
| **功能应用程序，GroupBy & windows**                          |                                                              |
| DataFrame.apply(func[, axis, broadcast, …])                  | 沿 DataFrame 的轴应用函数。                                  |
| DataFrame.applymap(func)                                     | 以元素方式将函数应用于 DataFrame。                           |
| DataFrame.pipe(func, *args, **kwargs)                        | 应用 func (自我，* args，* * kwargs)                         |
| DataFrame.agg(func[, axis])                                  | 使用指定轴上的一个或多个操作聚合。                           |
| DataFrame.aggregate(func[, axis])                            | 使用指定轴上的一个或多个操作聚合。                           |
| DataFrame.transform(func, *args, **kwargs)                   | 调用函数生成类似索引的 NDFrame，并返回带有转换值的 NDFrame   |
| DataFrame.groupby([by, axis, level, …])                      | 使用映射程序 (dict 或 key 函数，将给定函数应用于组，将结果作为 Series 返回) 或按一 Series 列对 Series 进行分组。 |
| DataFrame.rolling(window[, min_periods, …])                  | 提供滚动窗口计算。                                           |
| DataFrame.expanding([min_periods, center, axis])             | 提供扩展转换。                                               |
| DataFrame.ewm([com, span, halflife, alpha, …])               | 提供指数加权函数                                             |
| **计算 / 描述统计**                                          |                                                              |
| DataFrame.abs()                                              | 返回每个元素具有绝对值的 Series/DataFrame。                  |
| DataFrame.all([axis, bool_only, skipna, level])              | 返回 Series 轴或 DataFrame 轴上的所有元素是否为 True。       |
| DataFrame.any([axis, bool_only, skipna, level])              | 返回在请求的轴上是否有任何元素为真。                         |
| DataFrame.clip([lower, upper, axis, inplace])                | 输入阈值处的修剪值。                                         |
| DataFrame.clip_lower(threshold[, axis, inplace])             | 返回值低于阈值的输入副本被截断。                             |
| DataFrame.clip_upper(threshold[, axis, inplace])             | 返回截断值大于给定值的输入副本。                             |
| DataFrame.compound([axis, skipna, level])                    | 返回请求轴值的复合百分比                                     |
| DataFrame.corr([method, min_periods])                        | 计算列的成对相关性，不包括 NA /null 值                       |
| DataFrame.corrwith(other[, axis, drop])                      | 计算两个 DataFrame 对象的行或列之间的成对相关性。            |
| DataFrame.count([axis, level, numeric_only])                 | 对每列或每行的非 NA 单元格进行计数。                         |
| DataFrame.cov([min_periods])                                 | 计算列的成对协方差，不包括 NA /null 值。                     |
| DataFrame.cummax([axis, skipna])                             | 返回 DataFrame 或 Series 轴上的累积最大值。                  |
| DataFrame.cummin([axis, skipna])                             | 返回 DataFrame 或 Series 轴上的累积最小值。                  |
| DataFrame.cumprod([axis, skipna])                            | 通过 DataFrame 或 Series 轴返回累积产品。                    |
| DataFrame.cumsum([axis, skipna])                             | 返回 DataFrame 或 Series 轴上的累计总和。                    |
| DataFrame.describe([percentiles, include, …])                | 生成描述性统计数据，总结数据集分布的中心趋势、分散和形状，不包括 NaN 值。 |
| DataFrame.diff([periods, axis])                              | 元素的第一离散差。                                           |
| DataFrame.eval(expr[, inplace])                              | 评估描述 DataFrame 列操作的字符串。                          |
| DataFrame.kurt([axis, skipna, level, …])                     | 使用 Fisher 的峰度定义返回请求轴上的无偏峰度 (正常峰度 = = 0.0)。 |
| DataFrame.kurtosis([axis, skipna, level, …])                 | 使用 Fisher 的峰度定义返回请求轴上的无偏峰度 (正常峰度 = = 0.0)。 |
| DataFrame.mad([axis, skipna, level])                         | 返回请求轴值的平均绝对偏差                                   |
| DataFrame.max([axis, skipna, level, …])                      | 此方法返回对象中值的最大值。                                 |
| DataFrame.mean([axis, skipna, level, …])                     | 返回请求轴值的平均值                                         |
| DataFrame.median([axis, skipna, level, …])                   | 返回请求轴的值的中间值                                       |
| DataFrame.min([axis, skipna, level, …])                      | 此方法返回对象中值的最小值。                                 |
| DataFrame.mode([axis, numeric_only])                         | 获取每个元素沿选定轴的模式。                                 |
| DataFrame.pct_change([periods, fill_method, …])              | 当前元素和先前元素之间的百分比变化。                         |
| DataFrame.prod([axis, skipna, level, …])                     | 返回请求轴值的乘积                                           |
| DataFrame.product([axis, skipna, level, …])                  | 返回请求轴值的乘积                                           |
| DataFrame.quantile([q, axis, numeric_only, …])               | 在请求轴上给定分位数的返回值，la numpy . 百分位。            |
| DataFrame.rank([axis, method, numeric_only, …])              | 沿轴计算数值数据列 (1 到 n)。                                |
| DataFrame.round([decimals])                                  | 将 DataFrame 舍入到可变小数位数。                            |
| DataFrame.sem([axis, skipna, level, ddof, …])                | 返回请求轴上平均值的无偏标准误差。                           |
| DataFrame.skew([axis, skipna, level, …])                     | 返回由 N - 1 归一化的请求轴上的无偏歪斜                      |
| DataFrame.sum([axis, skipna, level, …])                      | 返回请求轴的值之和                                           |
| DataFrame.std([axis, skipna, level, ddof, …])                | 返回要求轴上的样品标准偏差。                                 |
| DataFrame.var([axis, skipna, level, ddof, …])                | 返回请求轴上的无偏方差。                                     |
| DataFrame.nunique([axis, dropna])                            | 返回在请求轴上有多个不同观察值的 Series。                    |
| **重新设计 / 选择 / 标签操作**                               |                                                              |
| DataFrame.add_prefix(prefix)                                 | 带字符串前缀的前缀标签。                                     |
| DataFrame.add_suffix(suffix)                                 | 带有字符串后缀的后缀标签。                                   |
| DataFrame.align(other[, join, axis, level, …])               | 将轴上的两个对象与每个轴索引的指定连接方法对齐               |
| DataFrame.at_time(time[, asof])                              | 选择一天中特定时间的值 (例如                                 |
| DataFrame.between_time(start_time, end_time)                 | 选择一天中特定时间之间的值 (例如，上午 9 : 00 - 9 : 30)。    |
| DataFrame.drop([labels, axis, index, …])                     | 从行或列中删除指定的标签。                                   |
| DataFrame.drop_duplicates([subset, keep, …])                 | 返回删除重复行的 DataFrame，可选地只考虑某些列               |
| DataFrame.duplicated([subset, keep])                         | 返回表示重复行的布尔 Series，可选地仅考虑某些列              |
| DataFrame.equals(other)                                      | 确定两个 NDFrame 对象是否包含相同的元素。                    |
| DataFrame.filter([items, like, regex, axis])                 | 根据指定索引中的标签子集 DataFrame 的行或列。                |
| DataFrame.first(offset)                                      | 基于日期偏移对时间 Series 数据初始周期进行细分的便捷方法。   |
| DataFrame.head([n])                                          | 返回前 n 行。                                                |
| DataFrame.idxmax([axis, skipna])                             | 返回请求轴上首次出现最大值的索引。                           |
| DataFrame.idxmin([axis, skipna])                             | 返回请求轴上第一次出现最小值的索引。                         |
| DataFrame.last(offset)                                       | 基于日期偏移对时间 Series 数据的最终周期进行细分的便捷方法。 |
| DataFrame.reindex([labels, index, columns, …])               | 用可选的填充逻辑使 DataFrame 符合新索引，将 NA / NaN 放置在前一个索引中没有值的位置。 |
| DataFrame.reindex_axis(labels[, axis, …])                    | 使用可选的填充逻辑使输入对象符合新索引，将 NA / NaN 放在先前索引中没有值的位置。 |
| DataFrame.reindex_like(other[, method, …])                   | 将具有匹配索引的对象返回给我自己。                           |
| DataFrame.rename([mapper, index, columns, …])                | 更改轴标签。                                                 |
| DataFrame.rename_axis(mapper[, axis, copy, …])               | 更改索引或列的名称。                                         |
| DataFrame.reset_index([level, drop, …])                      | 对于具有多级索引的 DataFrame，在索引名称下的列中返回带有标记信息的新 DataFrame，默认为 “level _ 0”、“level _ 1” 等。 |
| DataFrame.sample([n, frac, replace, …])                      | 从对象轴返回项目的随机样本。                                 |
| DataFrame.select(crit[, axis])                               | (已弃用) 返回与轴标签匹配条件相对应的数据                    |
| DataFrame.set_axis(labels[, axis, inplace])                  | 为给定轴指定所需的索引。                                     |
| DataFrame.set_index(keys[, drop, append, …])                 | 使用一个或多个现有列设置 DataFrame 索引 (行标签)。           |
| DataFrame.tail([n])                                          | 返回最后 n 行。                                              |
| DataFrame.take(indices[, axis, convert, is_copy])            | 沿轴返回给定位置索引中的元素。                               |
| DataFrame.truncate([before, after, axis, copy])              | 在某个索引值前后截断 Series 或 DataFrame。                   |
| **缺失数据处理**                                             |                                                              |
| DataFrame.dropna([axis, how, thresh, …])                     | 删除缺少的值。                                               |
| DataFrame.fillna([value, method, axis, …])                   | 使用指定的方法填写 NA / NaN 值                               |
| DataFrame.replace([to_replace, value, …])                    | 将 to _ replace 中给定的值替换为值。                         |
| DataFrame.interpolate([method, axis, limit, …])              | 根据不同的方法插值。                                         |
| **整形、分类、转移**                                         |                                                              |
| DataFrame.pivot([index, columns, values])                    | 返回按给定索引 / 列值组织的重新整形 DataFrame。              |
| DataFrame.pivot_table([values, index, …])                    | 创建电子表格样式的透视表作为 DataFrame 架。                  |
| DataFrame.reorder_levels(order[, axis])                      | 使用输入顺序重新排列索引级别。                               |
| DataFrame.sort_values(by[, axis, ascending, …])              | 按任一轴的值排序                                             |
| DataFrame.sort_index([axis, level, …])                       | 按标签 (沿轴) 排序对象                                       |
| DataFrame.nlargest(n, columns[, keep])                       | 按列降序返回前 n 行。                                        |
| DataFrame.nsmallest(n, columns[, keep])                      | 获取按列的 n 个最小值排序的 DataFrame 的行。                 |
| DataFrame.swaplevel([i, j, axis])                            | 交换特定轴上多索引中的级别 I 和 j                            |
| DataFrame.stack([level, dropna])                             | 将指定级别从列堆叠到索引。                                   |
| DataFrame.unstack([level, fill_value])                       | 枢转 (必须是分层的) 索引标签的级别，返回具有新级别的列标签的 DataFrame，该列标签的最内层由枢转的索引标签组成。 |
| DataFrame.swapaxes(axis1, axis2[, copy])                     | 适当交换轴和交换值轴                                         |
| DataFrame.melt([id_vars, value_vars, …])                     | “取消固定” 从宽格式到长格式的 DataFrame，可选地保留标识符变量集。 |
| DataFrame.squeeze([axis])                                    | 挤压长度 1 尺寸。                                            |
| DataFrame.to_panel()                                         | (已弃用) 将长 (堆叠) 格式 (DataFrame) 转换为宽 ( 3D、Panel) 格式。 |
| DataFrame.to_xarray()                                        | 从 Pandas 对象返回 xarray 对象。                             |
| DataFrame.T                                                  | 转置索引和列。                                               |
| DataFrame.transpose(*args, **kwargs)                         | 转置索引和列。                                               |
| **合并 / 加入 / 合并**                                       |                                                              |
| DataFrame.append(other[, ignore_index, …])                   | 将其他行追加到此帧的末尾，返回一个新对象。                   |
| DataFrame.assign(**kwargs)                                   | 将新列分配给 DataFrame，返回新对象 (副本)，新列添加到原始列中。 |
| DataFrame.join(other[, on, how, lsuffix, …])                 | 将列与索引或键列上的其他 DataFrame 连接起来。                |
| DataFrame.merge(right[, how, on, left_on, …])                | 通过按列或索引执行数据库样式的联接操作来合并 DataFrame 对象。 |
| DataFrame.update(other[, join, overwrite, …])                | 使用来自另一个 DataFrame 的非 NA 值就地修改。                |
| **时间 Series 相关的**                                       |                                                              |
| DataFrame.asfreq(freq[, method, how, …])                     | 将时间 Series 转换为指定频率。                               |
| DataFrame.asof(where[, subset])                              | 取不带 NaN 的最后一行 (或者在 DataFrame 的情况下，不带 NaN 的最后一行仅考虑列的子集) |
| DataFrame.shift([periods, freq, axis])                       | 按所需周期数移位索引，可选时间频率                           |
| DataFrame.slice_shift([periods, axis])                       | 相当于移位而不复制数据。                                     |
| DataFrame.tshift([periods, freq, axis])                      | 移动时间索引，使用索引的频率 (如果可用)。                    |
| DataFrame.first_valid_index()                                | 返回第一个非 NA /null 值的索引。                             |
| DataFrame.last_valid_index()                                 | 返回最后一个非 NA /null 值的索引。                           |
| DataFrame.resample(rule[, how, axis, …])                     | 时间 Series 频率转换和 Resampling 的便捷方法。               |
| DataFrame.to_period([freq, axis, copy])                      | 将 DataFrame 从 DatetimeIndex 转换为所需频率的周期索引 (如果没有通过，则从索引推断) |
| DataFrame.to_timestamp([freq, how, axis, copy])              | 转换为时间段开始时时间戳的日期时间索引                       |
| DataFrame.tz_convert(tz[, axis, level, copy])                | 将 tz 感知轴转换为目标时区。                                 |
| DataFrame.tz_localize(tz[, axis, level, …])                  | 将 tz - naive 时间 Series 本地化为目标时区。                 |
| **绘图**                                                     |                                                              |
| **DataFrame. plot 是表单 DataFrame. plot 的特定绘图方法的可调用方法和命名空间属性。** |                                                              |
| DataFrame.plot([x, y, kind, ax, ….])                         | DataFrame 绘图存取器和方法                                   |
| DataFrame.plot.area([x, y])                                  | 面积图                                                       |
| DataFrame.plot.bar([x, y])                                   | 竖线图。                                                     |
| DataFrame.plot.barh([x, y])                                  | 画一个横杠图。                                               |
| DataFrame.plot.box([by])                                     | 制作 DataFrame 列的方框图。                                  |
| DataFrame.plot.density([bw_method, ind])                     | 使用高斯核生成核密度估计图。                                 |
| DataFrame.plot.hexbin(x, y[, C, …])                          | 生成六边形宁滨图。                                           |
| DataFrame.plot.hist([by, bins])                              | 绘制 DataFrame 列的直方图。                                  |
| DataFrame.plot.kde([bw_method, ind])                         | 使用高斯核生成核密度估计图。                                 |
| DataFrame.plot.line([x, y])                                  | 将 DataFrame 列绘制为线。                                    |
| DataFrame.plot.pie([y])                                      | 生成饼图。                                                   |
| DataFrame.plot.scatter(x, y[, s, c])                         | 创建具有不同标记点大小和颜色的散点图。                       |
| DataFrame.boxplot([column, by, ax, …])                       | 从 DataFrame 列绘制方框图。                                  |
| DataFrame.hist([column, by, grid, …])                        | 制作 DataFrame 的直方图。                                    |
| **Series 化 / 输入输出 / 转换**                              |                                                              |
| DataFrame.from_csv(path[, header, sep, …])                   | (已弃用) 读取 CSV 文件。                                     |
| DataFrame.from_dict(data[, orient, dtype, …])                | 从数组状或 dict 的 dict 构造 DataFrame。                     |
| DataFrame.from_items(items[, columns, orient])               | (已弃用) 从元组列表中构建 DataFrame                          |
| DataFrame.from_records(data[, index, …])                     | 将结构化或记录数组转换为 DataFrame                           |
| DataFrame.info([verbose, buf, max_cols, …])                  | 打印 DataFrame 的简明摘要。                                  |
| DataFrame.to_parquet(fname[, engine, …])                     | 将 DataFrame 写入二进制拼花格式。                            |
| DataFrame.to_pickle(path[, compression, …])                  | 将对象保存 (Series 化) 到文件中。                            |
| DataFrame.to_csv([path_or_buf, sep, na_rep, …])              | 将 DataFrame 写入逗号分隔值 (CSV) 文件                       |
| DataFrame.to_hdf(path_or_buf, key, **kwargs)                 | 使用 HDFStore 将包含的数据写入 HDF5 文件。                   |
| DataFrame.to_sql(name, con[, schema, …])                     | 将存储在 DataFrame 中的记录写入 SQL 数据库。                 |
| DataFrame.to_dict([orient, into])                            | 将 DataFrame 转换为词典。                                    |
| DataFrame.to_excel(excel_writer[, …])                        | 将 DataFrame 写入 excel 工作表                               |
| DataFrame.to_json([path_or_buf, orient, …])                  | 将对象转换为 JSON 字符串。                                   |
| DataFrame.to_html([buf, columns, col_space, …])              | 将 DataFrame 渲染为 HTML 表。                                |
| DataFrame.to_feather(fname)                                  | 写出 DataFrame 的二进制羽化格式                              |
| DataFrame.to_latex([buf, columns, …])                        | 将对象呈现为表格环境表。                                     |
| DataFrame.to_stata(fname[, convert_dates, …])                | 导出 Stata 二进制 DTA 文件。                                 |
| DataFrame.to_msgpack([path_or_buf, encoding])                | msgpack (Series 化) 对象到输入文件路径                       |
| DataFrame.to_gbq(destination_table, project_id)              | 将 DataFrame 写入 Google BigQuery 表。                       |
| DataFrame.to_records([index, convert_datetime64])            | 将 DataFrame 转换为 NumPy 记录数组。                         |
| DataFrame.to_sparse([fill_value, kind])                      | 转换为稀疏塔夫兰                                             |
| DataFrame.to_dense()                                         | 返回 NDFrame 的密集表示 (相对于稀疏)                         |
| DataFrame.to_string([buf, columns, …])                       | 将 DataFrame 呈现为控制台友好的表格输出。                    |
| DataFrame.to_clipboard([excel, sep])                         | 将对象复制到系统剪贴板。                                     |
| DataFrame.style                                              | 属性返回 Styler 对象，该对象包含用于构建 DataFrame 架的样式化 HTML 表示的方法。 |
| **稀少的**                                                   |                                                              |
| SparseDataFrame.to_coo()                                     | 将帧内容作为稀疏的 SciPy COO 矩阵返回。                      |

## Panel

| 函数                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **构造器**                                                   |                                                              |
| Panel([data, items, major_axis, minor_axis, …])              | (已弃用) 表示宽格式 Panel 数据，存储为三维数组               |
| **属性和基础数据**                                           |                                                              |
| **轴线**                                                     |                                                              |
| **项目：轴 0；每个项目对应于包含在其中的 DataFrame**         |                                                              |
| **长轴：轴 1；每个 DataFrame 的索引 (行)**                   |                                                              |
| **短轴：轴 2；每个 DataFrame 的列**                          |                                                              |
| Panel.values                                                 | 返回 DataFrame 的 Numpy 表示形式。                           |
| Panel.axes                                                   | 返回内部 NDFrame 的索引标签                                  |
| Panel.ndim                                                   | 返回一个表示轴 / 数组维数的 int。                            |
| Panel.size                                                   | 返回一个 int，表示此对象中的元素数。                         |
| Panel.shape                                                  | 返回轴维元组                                                 |
| Panel.dtypes                                                 | 返回 DataFrame 中的数据类型。                                |
| Panel.ftypes                                                 | 返回 DataFrame 中的 ftype (稀疏 / 密集和 dtype 的指示)。     |
| Panel.get_dtype_counts()                                     | 返回此对象中唯一 dtypes 的计数。                             |
| Panel.get_ftype_counts()                                     | (已弃用) 返回此对象中唯一 ftypes 的计数。                    |
| **转变**                                                     |                                                              |
| Panel.astype(dtype[, copy, errors])                          | 将 Pandas 对象转换为指定的 dtype dtype。                     |
| Panel.copy([deep])                                           | 复制此对象的索引和数据。                                     |
| Panel.isna()                                                 | 检测缺失值。                                                 |
| Panel.notna()                                                | 检测现有 (未丢失) 值。                                       |
| **获取和设置**                                               |                                                              |
| Panel.get_value(*args, **kwargs)                             | (已弃用) 在 (项目、主要、次要) 位置快速检索单个值            |
| Panel.set_value(*args, **kwargs)                             | (已弃用) 在 (项目、主要、次要) 位置快速设置单个值            |
| **索引、迭代、切片**                                         |                                                              |
| Panel.at                                                     | 访问行 / 列标签对的单个值。                                  |
| Panel.iat                                                    | 按整数位置访问行 / 列对的单个值。                            |
| Panel.loc                                                    | 通过标签或布尔数组访问一组行和列。                           |
| Panel.iloc                                                   | 用于按位置选择的纯整数位置索引。                             |
| Panel.**iter**()                                             | 迭代信息轴                                                   |
| Panel.iteritems()                                            | 在信息轴上迭代 (标签，值)                                    |
| Panel.pop(item)                                              | 返回项目并从框架中删除。                                     |
| Panel.xs(key[, axis])                                        | 沿选定轴返回 Panel 切片                                      |
| Panel.major_xs(key)                                          | Panel 沿主轴返回片                                           |
| Panel.minor_xs(key)                                          | 沿短轴返回 Panel 切片                                        |
| **有关的更多信息。在。空运协会。锁定，和。iloc，请参阅索引文档。** |                                                              |
| **二元算子函数**                                             |                                                              |
| Panel.add(other[, axis])                                     | Series 和其他元素相加 (二进制运算符相加)。                   |
| Panel.sub(other[, axis])                                     | Series 减法和其他元素减法 (二进制运算符 sub)。               |
| Panel.mul(other[, axis])                                     | 级数与其他元素相乘 (二元运算符 mul)。                        |
| Panel.div(other[, axis])                                     | Series 和其他元素的浮动除法 (二元运算符 truediv)。           |
| Panel.truediv(other[, axis])                                 | Series 和其他元素的浮动除法 (二元运算符 truediv)。           |
| Panel.floordiv(other[, axis])                                | 按元素对 Series 和其他 Series 进行整数除法 (二进制运算符 flooddiv)。 |
| Panel.mod(other[, axis])                                     | Series 模和其他元素方式 (二进制运算符 mod)。                 |
| Panel.pow(other[, axis])                                     | 级数指数幂和其他元素幂 (二元算子幂)。                        |
| Panel.radd(other[, axis])                                    | 级数和其他元素相加 (二元算子 radd)。                         |
| Panel.rsub(other[, axis])                                    | Series 减法和其他元素减法 (二元运算符 rsub)。                |
| Panel.rmul(other[, axis])                                    | 级数与其他元素相乘 (二元运算符 rmul)。                       |
| Panel.rdiv(other[, axis])                                    | Series 和其他元素的浮动划分 (二元运算符 rtruediv)。          |
| Panel.rtruediv(other[, axis])                                | Series 和其他元素的浮动划分 (二元运算符 rtruediv)。          |
| Panel.rfloordiv(other[, axis])                               | 整数除法 Series 和其他，元素方式 (二元运算符 rfloordiv)。    |
| Panel.rmod(other[, axis])                                    | Series 模和其他元素 (二元运算符 rmod)。                      |
| Panel.rpow(other[, axis])                                    | 级数的指数幂和其他元素的指数幂 (二元算子 rpow)。             |
| Panel.lt(other[, axis])                                      | 比较法包装                                                   |
| Panel.gt(other[, axis])                                      | 比较法包装                                                   |
| Panel.le(other[, axis])                                      | 比较法用包装纸                                               |
| Panel.ge(other[, axis])                                      | 比较法通用电气包装                                           |
| Panel.ne(other[, axis])                                      | 比较法用包装纸                                               |
| Panel.eq(other[, axis])                                      | 比较法的包装                                                 |
| **功能应用程序**                                             |                                                              |
| Panel.apply(func[, axis])                                    | 沿 Panel 的轴应用功能                                        |
| Panel.groupby(function[, axis])                              | 给定轴上的组数据，返回 GroupBy 对象                          |
| **计算 / 描述统计**                                          |                                                              |
| Panel.abs()                                                  | 返回每个元素具有绝对值的 Series/DataFrame。                  |
| Panel.clip([lower, upper, axis, inplace])                    | 输入阈值处的修剪值。                                         |
| Panel.clip_lower(threshold[, axis, inplace])                 | 返回值低于阈值的输入副本被截断。                             |
| Panel.clip_upper(threshold[, axis, inplace])                 | 返回截断值大于给定值的输入副本。                             |
| Panel.count([axis])                                          | 返回请求轴上的观察次数。                                     |
| Panel.cummax([axis, skipna])                                 | 返回 DataFrame 或 Series 轴上的累积最大值。                  |
| Panel.cummin([axis, skipna])                                 | 返回 DataFrame 或 Series 轴上的累积最小值。                  |
| Panel.cumprod([axis, skipna])                                | 通过 DataFrame 或 Series 轴返回累积产品。                    |
| Panel.cumsum([axis, skipna])                                 | 返回 DataFrame 或 Series 轴上的累计总和。                    |
| Panel.max([axis, skipna, level, numeric_only])               | 此方法返回对象中值的最大值。                                 |
| Panel.mean([axis, skipna, level, numeric_only])              | 返回请求轴值的平均值                                         |
| Panel.median([axis, skipna, level, numeric_only])            | 返回请求轴的值的中间值                                       |
| Panel.min([axis, skipna, level, numeric_only])               | 此方法返回对象中值的最小值。                                 |
| Panel.pct_change([periods, fill_method, …])                  | 当前元素和先前元素之间的百分比变化。                         |
| Panel.prod([axis, skipna, level, …])                         | 返回请求轴值的乘积                                           |
| Panel.sem([axis, skipna, level, ddof, …])                    | 返回请求轴上平均值的无偏标准误差。                           |
| Panel.skew([axis, skipna, level, numeric_only])              | 返回由 N - 1 归一化的请求轴上的无偏歪斜                      |
| Panel.sum([axis, skipna, level, …])                          | 返回请求轴的值之和                                           |
| Panel.std([axis, skipna, level, ddof, …])                    | 返回要求轴上的样品标准偏差。                                 |
| Panel.var([axis, skipna, level, ddof, …])                    | 返回请求轴上的无偏方差。                                     |
| **重新设计 / 选择 / 标签操作**                               |                                                              |
| Panel.add_prefix(prefix)                                     | 带字符串前缀的前缀标签。                                     |
| Panel.add_suffix(suffix)                                     | 带有字符串后缀的后缀标签。                                   |
| Panel.drop([labels, axis, index, columns, …])                | -                                                            |
| Panel.equals(other)                                          | 确定两个 NDFrame 对象是否包含相同的元素。                    |
| Panel.filter([items, like, regex, axis])                     | 根据指定索引中的标签子集 DataFrame 的行或列。                |
| Panel.first(offset)                                          | 基于日期偏移对时间 Series 数据初始周期进行细分的便捷方法。   |
| Panel.last(offset)                                           | 基于日期偏移对时间 Series 数据的最终周期进行细分的便捷方法。 |
| Panel.reindex(*args, **kwargs)                               | 使 Panel 符合具有可选填充逻辑的新索引，将 NA / NaN 放置在前一索引中没有值的位置。 |
| Panel.reindex_axis(labels[, axis, method, …])                | 使用可选的填充逻辑使输入对象符合新索引，将 NA / NaN 放在先前索引中没有值的位置。 |
| Panel.reindex_like(other[, method, copy, …])                 | 将具有匹配索引的对象返回给我自己。                           |
| Panel.rename([items, major_axis, minor_axis])                | 改变轴输入功能。                                             |
| Panel.sample([n, frac, replace, weights, …])                 | 从对象轴返回项目的随机样本。                                 |
| Panel.select(crit[, axis])                                   | (已弃用) 返回与轴标签匹配条件相对应的数据                    |
| Panel.take(indices[, axis, convert, is_copy])                | 沿轴返回给定位置索引中的元素。                               |
| Panel.truncate([before, after, axis, copy])                  | 在某个索引值前后截断 Series 或 DataFrame。                   |
| **缺失数据处理**                                             |                                                              |
| Panel.dropna([axis, how, inplace])                           | 从 Panel 上放下 2D，保持通过的轴不变                         |
| **整形、分类、转移**                                         |                                                              |
| Panel.sort_index([axis, level, ascending, …])                | 按标签 (沿轴) 排序对象                                       |
| Panel.swaplevel([i, j, axis])                                | 交换特定轴上多索引中的级别 I 和 j                            |
| Panel.transpose(*args, **kwargs)                             | 更改 Panel 的尺寸                                            |
| Panel.swapaxes(axis1, axis2[, copy])                         | 适当交换轴和交换值轴                                         |
| Panel.conform(frame[, axis])                                 | 使输入 DataFrame 与所选轴对对齐。                            |
| **合并 / 加入 / 合并**                                       |                                                              |
| Panel.join(other[, how, lsuffix, rsuffix])                   | 在长轴和短轴列上将项目与其他 Panel 连接                      |
| Panel.update(other[, join, overwrite, …])                    | 使用传递 Panel 中的非 NA 值或可强制至 Panel 的对象将 Panel 修改到位。 |
| **时间 Series 相关的**                                       |                                                              |
| Panel.asfreq(freq[, method, how, normalize, …])              | 将时间 Series 转换为指定频率。                               |
| Panel.shift([periods, freq, axis])                           | 按所需周期数移位索引，可选时间频率。                         |
| Panel.resample(rule[, how, axis, …])                         | 时间 Series 频率转换和 Resampling 的便捷方法。               |
| Panel.tz_convert(tz[, axis, level, copy])                    | 将 tz 感知轴转换为目标时区。                                 |
| Panel.tz_localize(tz[, axis, level, copy, …])                | 将 tz - naive 时间 Series 本地化为目标时区。                 |
| **Series 化 / 输入输出 / 转换**                              |                                                              |
| Panel.from_dict(data[, intersect, orient, dtype])            | 从 DataFrame 对象的 dict 构造 Panel                          |
| Panel.to_pickle(path[, compression, protocol])               | 将对象保存 (Series 化) 到文件中。                            |
| Panel.to_excel(path[, na_rep, engine])                       | 将 Panel 中的每个 DataFrame 写入单独的 excel 工作表          |
| Panel.to_hdf(path_or_buf, key, **kwargs)                     | 使用 HDFStore 将包含的数据写入 HDF5 文件。                   |
| Panel.to_sparse(*args, **kwargs)                             | 未实现：不要调用此方法，因为 Panel 对象不支持稀疏化，这将引发错误。 |
| Panel.to_frame([filter_observations])                        | 将宽格式转换为长 (堆叠) 格式作为 DataFrame，DataFrame 的列是 Panel 的项，索引是由 Panel 的长轴和短轴组成的多索引。 |
| Panel.to_clipboard([excel, sep])                             | 将对象复制到系统剪贴板。                                     |

## 索引

| 函数                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **在包含索引 (Series/DataFrame) 的对象上可以获得这些方法或其变体中的许多，这些方法或变体最有可能在直接调用这些方法之前使用。** |                                                              |
| Index                                                        | 不可变的 ndarray 实现有序的、可切片的集合。                  |
| **属性**                                                     |                                                              |
| Index.values                                                 | 以 ndarray 形式返回基础数据                                  |
| Index.is_monotonic                                           | 别名为 is _ monotical _ exporting (已弃用)                   |
| Index.is_monotonic_increasing                                | 如果索引是单调递增 (仅相等或递增) 值，则返回。               |
| Index.is_monotonic_decreasing                                | 如果索引是单调递减 (仅相等或递减) 值，则返回。               |
| Index.is_unique                                              | 如果索引具有唯一值，则返回                                   |
| Index.has_duplicates                                         | -                                                            |
| Index.hasnans                                                | 如果我有南社就回来；启用各种性能加速                         |
| Index.dtype                                                  | 返回基础数据的 dtype 对象                                    |
| Index.dtype_str                                              | 返回基础数据的 dtype 字符串                                  |
| Index.inferred_type                                          | 返回从值推断的类型的字符串                                   |
| Index.is_all_dates                                           | -                                                            |
| Index.shape                                                  | 返回基础数据形状的元组                                       |
| Index.name                                                   | -                                                            |
| Index.names                                                  | -                                                            |
| Index.nbytes                                                 | 返回基础数据中的字节数                                       |
| Index.ndim                                                   | 根据定义 1 返回基础数据的维数                                |
| Index.size                                                   | 返回基础数据中的元素数                                       |
| Index.empty                                                  | -                                                            |
| Index.strides                                                | 返回基础数据的步长                                           |
| Index.itemsize                                               | 返回基础数据项的 dtype 大小                                  |
| Index.base                                                   | 如果共享基础数据的内存，则返回基对象                         |
| Index.T                                                      | 返回转置，这是自我定义                                       |
| Index.memory_usage([deep])                                   | 值的内存使用                                                 |
| **修改和计算**                                               |                                                              |
| Index.all(*args, **kwargs)                                   | 返回所有元素是否为真。                                       |
| Index.any(*args, **kwargs)                                   | 返回任何元素是否为真。                                       |
| Index.argmin([axis])                                         | 返回最小参数索引器的 ndarray                                 |
| Index.argmax([axis])                                         | 返回最大参数索引器的 ndarray                                 |
| Index.copy([name, deep, dtype])                              | 复制此对象。                                                 |
| Index.delete(loc)                                            | 删除传递位置为 (- s) 的新索引                                |
| Index.drop(labels[, errors])                                 | 创建新索引，删除传递的标签列表                               |
| Index.drop_duplicates([keep])                                | 返回删除重复值的索引。                                       |
| Index.duplicated([keep])                                     | 指示重复的索引值。                                           |
| Index.equals(other)                                          | 确定两个索引对象是否包含相同的元素。                         |
| Index.factorize([sort, na_sentinel])                         | 将对象编码为枚举类型或分类变量。                             |
| Index.identical(other)                                       | 类似于 equals，但检查其他类似属性是否也相同                  |
| Index.insert(loc, item)                                      | 制作新索引在位置插入新项目。                                 |
| Index.is_(other)                                             | 更灵活、更快速的检查就像是，但这可以通过视图来实现           |
| Index.is_boolean()                                           | -                                                            |
| Index.is_categorical()                                       | 检查索引是否包含分类数据。                                   |
| Index.is_floating()                                          | -                                                            |
| Index.is_integer()                                           | -                                                            |
| Index.is_interval()                                          | -                                                            |
| Index.is_lexsorted_for_tuple(tup)                            | -                                                            |
| Index.is_mixed()                                             | -                                                            |
| Index.is_numeric()                                           | -                                                            |
| Index.is_object()                                            | -                                                            |
| Index.min()                                                  | 返回索引的最小值。                                           |
| Index.max()                                                  | 返回索引的最大值。                                           |
| Index.reindex(target[, method, level, …])                    | 使用目标值创建索引 (根据需要移动 / 添加 / 删除值)            |
| Index.rename(name[, inplace])                                | 在索引上设置新名称。                                         |
| Index.repeat(repeats, *args, **kwargs)                       | 重复索引的元素。                                             |
| Index.where(cond[, other])                                   | -                                                            |
| Index.take(indices[, axis, allow_fill, …])                   | 返回索引所选值的新索引                                       |
| Index.putmask(mask, value)                                   | 返回使用掩码设置的值的新索引                                 |
| Index.set_names(names[, level, inplace])                     | 在索引上设置新名称。                                         |
| Index.unique([level])                                        | 返回索引中的唯一值。                                         |
| Index.nunique([dropna])                                      | 返回对象中唯一元素的数目。                                   |
| Index.value_counts([normalize, sort, …])                     | 返回包含唯一值计数的对象。                                   |
| **缺失值**                                                   |                                                              |
| Index.fillna([value, downcast])                              | 用指定值填充 NA / NaN 值                                     |
| Index.dropna([how])                                          | 没有 NA / NaN 值的返回索引                                   |
| Index.isna()                                                 | 检测缺失值。                                                 |
| Index.notna()                                                | 检测现有 (未丢失) 值。                                       |
| **转变**                                                     |                                                              |
| Index.astype(dtype[, copy])                                  | 创建具有转换为 dtypes 的值的索引。                           |
| Index.item()                                                 | 以 python 标量形式返回基础数据的第一个元素                   |
| Index.map(mapper[, na_action])                               | 使用输入对应关系映射值 (dict、Series 或函数)。               |
| Index.ravel([order])                                         | 返回基础数据的展平值的数组                                   |
| Index.tolist()                                               | 返回值列表。                                                 |
| Index.to_native_types([slicer])                              | 格式化 self 的指定值并返回它们。                             |
| Index.to_series([index, name])                               | 创建一个索引和值都等于索引键的 Series，该索引键与 map 一起用于基于索引返回索引器 |
| Index.to_frame([index])                                      | 使用包含索引的列创建 DataFrame。                             |
| Index.view([cls])                                            | -                                                            |
| **整理**                                                     |                                                              |
| Index.argsort(*args, **kwargs)                               | 返回对索引进行排序的整数标记。                               |
| Index.searchsorted(value[, side, sorter])                    | 查找应该插入元素以维持秩序的索引。                           |
| Index.sort_values([return_indexer, ascending])               | 返回索引的排序副本。                                         |
| **特定时间操作**                                             |                                                              |
| Index.shift([periods, freq])                                 | 按所需的时间频率增量数移位索引。                             |
| **组合 / 连接 / 设置操作**                                   |                                                              |
| Index.append(other)                                          | 将索引选项集合附加在一起                                     |
| Index.join(other[, how, level, …])                           | 这是一种内部非公开的方法                                     |
| Index.intersection(other)                                    | 形成两个索引对象的交集。                                     |
| Index.union(other)                                           | 形成两个索引对象的并集，并尽可能进行排序。                   |
| Index.difference(other)                                      | 返回一个新索引，其中包含索引中不在其他位置的元素。           |
| Index.symmetric_difference(other[, result_name])             | 计算两个索引对象的对称差。                                   |
| **选择**                                                     |                                                              |
| Index.asof(label)                                            | 对于排序的索引，返回直到并包括传递的标签的最新标签。         |
| Index.asof_locs(where, mask)                                 | 其中：时间戳掩码数组：数据不是 NA 的布尔数组                 |
| Index.contains(key)                                          | 如果此键在索引中，则返回布尔值                               |
| Index.get_duplicates()                                       | (已弃用) 提取重复的索引元素。                                |
| Index.get_indexer(target[, method, limit, …])                | 计算给定当前索引的新索引的索引器和掩码。                     |
| Index.get_indexer_for(target, **kwargs)                      | 即使在不唯一的情况下，也保证返回索引器，这将根据需要分派给 get _ indexer 或 get _ indexer _ uninique |
| Index.get_indexer_non_unique(target)                         | 计算给定当前索引的新索引的索引器和掩码。                     |
| Index.get_level_values(level)                                | 返回请求级别的值索引，等于索引的长度。                       |
| Index.get_loc(key[, method, tolerance])                      | 获取请求标签整数位置，切片或布尔掩码。                       |
| Index.get_slice_bound(label, side, kind)                     | 计算与给定标签相对应的切片边界。                             |
| Index.get_value(series, key)                                 | 从一维数组快速查找值。                                       |
| Index.get_values()                                           | 以数字形式返回索引数据                                       |
| Index.set_value(arr, key, value)                             | 从一维数组快速查找值。                                       |
| Index.isin(values[, level])                                  | 返回索引值以值为单位的布尔数组。                             |
| Index.slice_indexer([start, end, step, kind])                | 对于有序或唯一索引，计算输入标签和步骤的切片索引器。         |
| Index.slice_locs([start, end, step, kind])                   | 计算输入标签的切片位置。                                     |
| **数字索引**                                                 |                                                              |
| RangeIndex                                                   | 实现单调整数范围的不可变索引。                               |
| Int64Index                                                   | 不可变的 ndarray 实现有序的、可切片的集合。                  |
| UInt64Index                                                  | 不可变的 ndarray 实现有序的、可切片的集合。                  |
| Float64Index                                                 | 不可变的 ndarray 实现有序的、可切片的集合。                  |
| RangeIndex.from_range(data[, name, dtype])                   | 从范围 (py3) 或 xrange ( py2 ) 对象创建范围索引              |
| **范畴尺度指数**                                             |                                                              |
| CategoricalIndex                                             | 实现有序、可切片集合的不可变索引。                           |
| **范畴成分**                                                 |                                                              |
| CategoricalIndex.codes                                       | -                                                            |
| CategoricalIndex.categories                                  | -                                                            |
| CategoricalIndex.ordered                                     | -                                                            |
| CategoricalIndex.rename_categories(*args, …)                 | 重命名类别。                                                 |
| CategoricalIndex.reorder_categories(*args, …)                | 按照 new _ categories 中的指定重新排序类别。                 |
| CategoricalIndex.add_categories(*args, **kwargs)             | 添加新类别。                                                 |
| CategoricalIndex.remove_categories(*args, …)                 | 删除指定的类别。                                             |
| CategoricalIndex.remove_unused_categories(…)                 | 删除未使用的类别。                                           |
| CategoricalIndex.set_categories(*args, **kwargs)             | 将类别设置为指定的 new _ categories。                        |
| CategoricalIndex.as_ordered(*args, **kwargs)                 | 设置要排序的分类                                             |
| CategoricalIndex.as_unordered(*args, **kwargs)               | 将分类设置为无序                                             |
| CategoricalIndex.map(mapper)                                 | 使用输入对应关系映射值 (dict、Series 或函数)。               |
| **internalindex**                                            |                                                              |
| IntervalIndex                                                | 实现有序、可切片集合的不可变索引。                           |
| **internalindex 组件**                                       |                                                              |
| IntervalIndex.from_arrays(left, right[, …])                  | 由定义左右边界的两个数组构造。                               |
| IntervalIndex.from_tuples(data[, closed, …])                 | 从元组列表 / 数组中构建 internalindex                        |
| IntervalIndex.from_breaks(breaks[, closed, …])               | 从拆分数组构造 internalindex                                 |
| IntervalIndex.contains(key)                                  | 返回一个布尔值，指示键是否在索引中                           |
| IntervalIndex.left                                           | 返回 internalindex 中每个间隔的左端点作为索引                |
| IntervalIndex.right                                          | 返回 internalindex 中每个间隔的右端点作为索引                |
| IntervalIndex.mid                                            | 返回 internalindex 中每个间隔的中点作为索引                  |
| IntervalIndex.closed                                         | 间隔是在左侧、右侧关闭，还是两者都关闭                       |
| IntervalIndex.length                                         | 返回一个索引，其中的条目表示 internalindex 中每个间隔的长度  |
| IntervalIndex.values                                         | 将 internalindex 的数据作为间隔对象的 numpy 数组返回 (dtype = ' object ') |
| IntervalIndex.is_non_overlapping_monotonic                   | 如果 internalindex 不重叠 (无间隔共享点)，并且单调递增或单调递减，则返回 True，否则返回 False |
| IntervalIndex.get_loc(key[, method])                         | 获取请求标签整数位置，切片或布尔掩码。                       |
| IntervalIndex.get_indexer(target[, method, …])               | 计算给定当前索引的新索引的索引器和掩码。                     |
| **多指标**                                                   |                                                              |
| MultiIndex                                                   | Pandas 对象的多级或分层索引对象                              |
| IndexSlice                                                   | 创建对象以更轻松地执行多索引切片                             |
| **多指标构造函数**                                           |                                                              |
| MultiIndex.from_arrays(arrays[, sortorder, …])               | 将数组转换为多索引                                           |
| MultiIndex.from_tuples(tuples[, sortorder, …])               | 将元组列表转换为多索引                                       |
| MultiIndex.from_product(iterables[, …])                      | 由多个可滴定物的笛卡儿积建立多指标                           |
| **多指标属性**                                               |                                                              |
| MultiIndex.names                                             | 多重索引中的层级名称                                         |
| MultiIndex.levels                                            | -                                                            |
| MultiIndex.labels                                            | -                                                            |
| MultiIndex.nlevels                                           | 此多重索引中的整数层级。                                     |
| MultiIndex.levshape                                          | 具有每个级别长度的元组。                                     |
| **多指标成分**                                               |                                                              |
| MultiIndex.set_levels(levels[, level, …])                    | 在多索引上设置新级别。                                       |
| MultiIndex.set_labels(labels[, level, …])                    | 在多索引上设置新标签。                                       |
| MultiIndex.to_hierarchical(n_repeat[, n_shuffle])            | 返回重新整形的多索引，以符合 n _ repeat 和 n _ shuffle 给定的形状。 |
| MultiIndex.to_frame([index])                                 | 以多索引级别为列创建 DataFrame。                             |
| MultiIndex.is_lexsorted()                                    | 如果标签按字典顺序排序，则返回 True                          |
| MultiIndex.sortlevel([level, ascending, …])                  | 在请求的级别排序多索引。                                     |
| MultiIndex.droplevel([level])                                | 移除要求层级的传回索引。                                     |
| MultiIndex.swaplevel([i, j])                                 | 用 j 级交换一级                                              |
| MultiIndex.reorder_levels(order)                             | 使用输入顺序重新排列级别。                                   |
| MultiIndex.remove_unused_levels()                            | 从当前创建一个新的多索引，以删除未使用的级别，这意味着它们不会在标签中表达 |
| MultiIndex.unique([level])                                   | 返回索引中的唯一值。                                         |
| **多指标选择**                                               |                                                              |
| MultiIndex.get_loc(key[, method])                            | 获取作为整数、切片或布尔掩码的标签或标签元组的位置。         |
| MultiIndex.get_indexer(target[, method, …])                  | 计算给定当前索引的新索引的索引器和掩码。                     |
| MultiIndex.get_level_values(level)                           | 返回请求级别的标签值向量，等于索引的长度。                   |
| **日期时间索引**                                             |                                                              |
| DatetimeIndex                                                | datetime64 数据的不可变的 ndarray，内部表示为 int 64，它可以被装箱到作为 datetime 子类的时间戳对象中，并携带诸如频率信息之类的元数据。 |
| **时间 / 日期组成部分**                                      |                                                              |
| DatetimeIndex.year                                           | 日期时间的年份                                               |
| DatetimeIndex.month                                          | 1 月 = 1 月，12 月 = 12 月                                   |
| DatetimeIndex.day                                            | 日期时间的天数                                               |
| DatetimeIndex.hour                                           | 日期时间的小时数                                             |
| DatetimeIndex.minute                                         | 日期时间的分钟数                                             |
| DatetimeIndex.second                                         | 日期时间的秒数                                               |
| DatetimeIndex.microsecond                                    | 日期时间的微秒                                               |
| DatetimeIndex.nanosecond                                     | 日期时间的纳秒                                               |
| DatetimeIndex.date                                           | 返回 python datetime . date 对象的 numpy 数组 (即时间戳中没有时区信息的日期部分)。 |
| DatetimeIndex.time                                           | 返回 datetime . time 的 numpy 数组。                         |
| DatetimeIndex.dayofyear                                      | 一年中的第几天                                               |
| DatetimeIndex.weekofyear                                     | 一年中的第几周                                               |
| DatetimeIndex.week                                           | 一年中的第几周                                               |
| DatetimeIndex.dayofweek                                      | 星期一 = 0，星期日 = 6 的星期几                              |
| DatetimeIndex.weekday                                        | 星期一 = 0，星期日 = 6 的星期几                              |
| DatetimeIndex.quarter                                        | 日期的季度                                                   |
| DatetimeIndex.tz                                             | -                                                            |
| DatetimeIndex.freq                                           | 如果设置了 frequency 对象，则返回该对象，否则无              |
| DatetimeIndex.freqstr                                        | 如果设置了 frequency 对象，则将其作为字符串返回，否则无      |
| DatetimeIndex.is_month_start                                 | 逻辑指示每月第一天 (由频率定义)                              |
| DatetimeIndex.is_month_end                                   | 指示日期是否为当月的最后一天。                               |
| DatetimeIndex.is_quarter_start                               | 指示日期是否为季度的第一天。                                 |
| DatetimeIndex.is_quarter_end                                 | 指示日期是否为季度的最后一天。                               |
| DatetimeIndex.is_year_start                                  | 指出日期是否为一年中的第一天。                               |
| DatetimeIndex.is_year_end                                    | 指出日期是否为一年中的最后一天。                             |
| DatetimeIndex.is_leap_year                                   | 如果日期属于闰年，则为布尔指示符。                           |
| DatetimeIndex.inferred_freq                                  | 尝试返回一个 string 类型的值，该值代表由 inversion _ freq 生成的频率猜测。 |
| **选择**                                                     |                                                              |
| DatetimeIndex.indexer_at_time(time[, asof])                  | 返回索引值在一天中特定时间的索引位置 (例如                   |
| DatetimeIndex.indexer_between_time(…[, …])                   | 返回一天中特定时间 (例如 9 : 00 - 9 : 30) 之间的值的索引位置。 |
| **特定时间操作**                                             |                                                              |
| DatetimeIndex.normalize()                                    | 将时间转换为午夜。                                           |
| DatetimeIndex.strftime(date_format)                          | 使用指定的 date _ format 转换为索引。                        |
| DatetimeIndex.snap([freq])                                   | 将时间戳捕捉到最近出现的频率                                 |
| DatetimeIndex.tz_convert(tz)                                 | 将 tz 感知的日期时间索引从一个时区转换到另一个时区。         |
| DatetimeIndex.tz_localize(tz[, ambiguous, …])                | 将 tz - naive 日期时间索引本地化为 tz 感知的日期时间索引。   |
| DatetimeIndex.round(freq, *args, **kwargs)                   | 将数据舍入到指定的频率。                                     |
| DatetimeIndex.floor(freq)                                    | 将数据降至指定频率。                                         |
| DatetimeIndex.ceil(freq)                                     | 将数据上限设置为指定频率。                                   |
| DatetimeIndex.month_name([locale])                           | 返回具有指定区域设置的 DateTimeIndex 的月份名称。            |
| DatetimeIndex.day_name([locale])                             | 返回具有指定区域设置的 DateTimeIndex 的日期名称。            |
| **转变**                                                     |                                                              |
| DatetimeIndex.to_period([freq])                              | 以特定频率转换为周期指数。                                   |
| DatetimeIndex.to_perioddelta(freq)                           | 计算指标值与按指定频率转换为周期指标的指标之间差值的时间增量指标。 |
| DatetimeIndex.to_pydatetime()                                | 返回 DatetimeIndex 作为 datetime . datetime 对象的对象数组   |
| DatetimeIndex.to_series([keep_tz, index, name])              | 创建一个索引和值都等于索引键的 Series，该索引键与 map 一起用于基于索引返回索引器 |
| DatetimeIndex.to_frame([index])                              | 使用包含索引的列创建 DataFrame。                             |
| **时间增量指数**                                             |                                                              |
| TimedeltaIndex                                               | timedelta 64 数据的不可变数组，内部表示为 int 64，可以装箱到 timedelta 对象中 |
| **成分**                                                     |                                                              |
| TimedeltaIndex.days                                          | 每个元素的天数。                                             |
| TimedeltaIndex.seconds                                       | 每个元素的秒数 (> = 0 且小于 1 天)。                         |
| TimedeltaIndex.microseconds                                  | 每个元素的微秒数 (> = 0 且小于 1 秒)。                       |
| TimedeltaIndex.nanoseconds                                   | 每个元素的纳秒数 (> = 0 且小于 1 微秒)。                     |
| TimedeltaIndex.components                                    | 返回时间增量组件的 DataFrame (天、小时、分钟、秒、毫秒、微秒、纳秒)。 |
| TimedeltaIndex.inferred_freq                                 | 尝试返回一个 string 类型的值，该值代表由 inversion _ freq 生成的频率猜测。 |
| **转变**                                                     |                                                              |
| TimedeltaIndex.to_pytimedelta()                              | 将 timedeltindex 作为 datetimedelta 对象的对象数组返回       |
| TimedeltaIndex.to_series([index, name])                      | 创建一个索引和值都等于索引键的 Series，该索引键与 map 一起用于基于索引返回索引器 |
| TimedeltaIndex.round(freq, *args, **kwargs)                  | 将数据舍入到指定的频率。                                     |
| TimedeltaIndex.floor(freq)                                   | 将数据降至指定频率。                                         |
| TimedeltaIndex.ceil(freq)                                    | 将数据上限设置为指定频率。                                   |
| TimedeltaIndex.to_frame([index])                             | 使用包含索引的列创建 DataFrame。                             |
| **周期指数**                                                 |                                                              |
| PeriodIndex                                                  | 毫无疑问，ndarray holding ordinal values indirect regular periods of such as a special years，quarters，months，等等，这些都是在这些年份中经常出现的情况。 |
| **属性**                                                     |                                                              |
| PeriodIndex.day                                              | 期间的天数                                                   |
| PeriodIndex.dayofweek                                        | 星期一 = 0，星期日 = 6 的星期几                              |
| PeriodIndex.dayofyear                                        | 一年中的第几天                                               |
| PeriodIndex.days_in_month                                    | 当月的天数                                                   |
| PeriodIndex.daysinmonth                                      | 当月的天数                                                   |
| PeriodIndex.end_time                                         | -                                                            |
| PeriodIndex.freq                                             | 如果设置了 frequency 对象，则返回该对象，否则无              |
| PeriodIndex.freqstr                                          | 如果设置了 frequency 对象，则将其作为字符串返回，否则无      |
| PeriodIndex.hour                                             | 时段的时间                                                   |
| PeriodIndex.is_leap_year                                     | 逻辑指示日期是否属于闰年                                     |
| PeriodIndex.minute                                           | 时段的分钟                                                   |
| PeriodIndex.month                                            | 1 月 = 1 月，12 月 = 12 月                                   |
| PeriodIndex.quarter                                          | 日期的季度                                                   |
| PeriodIndex.qyear                                            | -                                                            |
| PeriodIndex.second                                           | 第二阶段                                                     |
| PeriodIndex.start_time                                       | -                                                            |
| PeriodIndex.week                                             | 一年中的第几周                                               |
| PeriodIndex.weekday                                          | 星期一 = 0，星期日 = 6 的星期几                              |
| PeriodIndex.weekofyear                                       | 一年中的第几周                                               |
| PeriodIndex.year                                             | 期间的年份                                                   |
| **方法**                                                     |                                                              |
| PeriodIndex.asfreq([freq, how])                              | 将周期指数转换为指定的频率频率。                             |
| PeriodIndex.strftime(date_format)                            | 使用指定的 date _ format 转换为索引。                        |
| PeriodIndex.to_timestamp([freq, how])                        | 转换为日期时间索引                                           |
| PeriodIndex.tz_convert(tz)                                   | 将 tz 感知的日期时间索引从一个时区转换到另一个时区 (使用 pytz /dateutil) |
| PeriodIndex.tz_localize(tz[, ambiguous])                     | 将 tz - naive datetimendix 本地化为给定时区 (使用 pytz /dateutil)，或从 tz 感知的 datetimendix 中删除时区 |
| **标量**                                                     |                                                              |
| **时期**                                                     |                                                              |
| Period                                                       | 代表一段时间                                                 |
| **属性**                                                     |                                                              |
| Period.day                                                   | 获取某个时间段所在月份的日期。                               |
| Period.dayofweek                                             | 返回星期几。                                                 |
| Period.dayofyear                                             | 返回一年中的某一天。                                         |
| Period.days_in_month                                         | 获取此期间所在月份的总天数。                                 |
| Period.daysinmonth                                           | 获取期间所在月份的总天数。                                   |
| Period.end_time                                              | -                                                            |
| Period.freq                                                  | -                                                            |
| Period.freqstr                                               | -                                                            |
| Period.hour                                                  | 获取时间段中的一天中的小时数。                               |
| Period.is_leap_year                                          | -                                                            |
| Period.minute                                                | 获取时间段的小时组成部分的分钟数。                           |
| Period.month                                                 | -                                                            |
| Period.ordinal                                               | -                                                            |
| Period.quarter                                               | -                                                            |
| Period.qyear                                                 | -                                                            |
| Period.second                                                | 获取周期的第二部分。                                         |
| Period.start_time                                            | 获取周期开始的时间戳。                                       |
| Period.week                                                  | 获取给定时间段内的一年中的一周。                             |
| Period.weekday                                               | -                                                            |
| Period.weekofyear                                            | -                                                            |
| Period.year                                                  | -                                                            |
| **方法**                                                     |                                                              |
| Period.asfreq                                                | 在间隔开始或结束时，将周期转换为所需频率                     |
| Period.now                                                   | -                                                            |
| Period.strftime                                              | 根据选定的 fmt 返回周期的字符串表示形式。                    |
| Period.to_timestamp                                          | 返回指定周期结束 (方式) 时目标频率上周期的时间戳表示         |
| **时间戳**                                                   |                                                              |
| Timestamp                                                    | Pandas 替换日期时间                                          |
| **性能**                                                     |                                                              |
| Timestamp.asm8                                               | -                                                            |
| Timestamp.day                                                | -                                                            |
| Timestamp.dayofweek                                          | -                                                            |
| Timestamp.dayofyear                                          | -                                                            |
| Timestamp.days_in_month                                      | -                                                            |
| Timestamp.daysinmonth                                        | -                                                            |
| Timestamp.fold                                               | -                                                            |
| Timestamp.hour                                               | -                                                            |
| Timestamp.is_leap_year                                       | -                                                            |
| Timestamp.is_month_end                                       | -                                                            |
| Timestamp.is_month_start                                     | -                                                            |
| Timestamp.is_quarter_end                                     | -                                                            |
| Timestamp.is_quarter_start                                   | -                                                            |
| Timestamp.is_year_end                                        | -                                                            |
| Timestamp.is_year_start                                      | -                                                            |
| Timestamp.max                                                | -                                                            |
| Timestamp.microsecond                                        | -                                                            |
| Timestamp.min                                                | -                                                            |
| Timestamp.minute                                             | -                                                            |
| Timestamp.month                                              | -                                                            |
| Timestamp.nanosecond                                         | -                                                            |
| Timestamp.quarter                                            | -                                                            |
| Timestamp.resolution                                         | -                                                            |
| Timestamp.second                                             | -                                                            |
| Timestamp.tz                                                 | tzinfo 的别名                                                |
| Timestamp.tzinfo                                             | -                                                            |
| Timestamp.value                                              | -                                                            |
| Timestamp.week                                               | -                                                            |
| Timestamp.weekofyear                                         | -                                                            |
| Timestamp.year                                               | -                                                            |
| **方法**                                                     |                                                              |
| Timestamp.astimezone                                         | 将 tz 感知时间戳转换为另一个时区。                           |
| Timestamp.ceil                                               | 返回导致此解决方案的新时间戳                                 |
| Timestamp.combine(date, time)                                | 日期、时间 - > 日期时间，具有相同的日期和时间字段            |
| Timestamp.ctime                                              | 返回 ctime ( ) 样式字符串。                                  |
| Timestamp.date                                               | 返回年、月、日相同日期对象。                                 |
| Timestamp.day_name                                           | 返回具有指定区域设置的时间戳的日期名称。                     |
| Timestamp.dst                                                | 返回自我。                                                   |
| Timestamp.floor                                              | 返回此分辨率下的新时间戳                                     |
| Timestamp.freq                                               | -                                                            |
| Timestamp.freqstr                                            | -                                                            |
| Timestamp.fromordinal(ordinal[, freq, tz])                   | 传递序号，翻译并转换为 ts 注释：根据定义，序号本身不能有任何 tz 信息 |
| Timestamp.fromtimestamp(ts)                                  | 时间戳 [，tz] - > 从 POSIX 时间戳开始的 tz 本地时间。        |
| Timestamp.isocalendar                                        | 返回包含 ISO 年、周数和工作日的三元组。                      |
| Timestamp.isoformat                                          | -                                                            |
| Timestamp.isoweekday                                         | 返回日期所代表的星期几。                                     |
| Timestamp.month_name                                         | 返回具有指定区域设置的时间戳的月份名称。                     |
| Timestamp.normalize                                          | 将时间戳标准化到午夜，保留 tz 信息。                         |
| Timestamp.now([tz])                                          | 返回表示 tz 本地当前时间的新时间戳对象。                     |
| Timestamp.replace                                            | 实现日期时间。替换，处理纳秒                                 |
| Timestamp.round                                              | 将时间戳舍入到指定的分辨率                                   |
| Timestamp.strftime                                           | 格式 - > strftime ( ) 样式字符串。                           |
| Timestamp.strptime                                           | string，format - - > 从字符串解析的新日期时间 (如 time . strptime () )。 |
| Timestamp.time                                               | 返回时间相同但 tzinfo = 无的时间对象。                       |
| Timestamp.timestamp                                          | 以浮点形式返回 POSIX 时间戳。                                |
| Timestamp.timetuple                                          | 返回时间元组，与时间兼容。localtime ( )。                    |
| Timestamp.timetz                                             | 返回具有相同时间和 tzinfo 的时间对象。                       |
| Timestamp.to_datetime64                                      | 返回一个精度为 “ns” 的 numpy . datetime64 对象               |
| Timestamp.to_julian_date                                     | 将时间戳转换为儒略日。                                       |
| Timestamp.to_period                                          | 返回此时间戳为观察值的时间段。                               |
| Timestamp.to_pydatetime                                      | 将时间戳对象转换为本机 Python datetime 对象。                |
| Timestamp.today(cls[, tz])                                   | 返回本地时区中的当前时间。                                   |
| Timestamp.toordinal                                          | 返回无理期公历序数。                                         |
| Timestamp.tz_convert                                         | 将 tz 感知时间戳转换为另一个时区。                           |
| Timestamp.tz_localize                                        | 将原始时间戳转换为本地时区，或从 tz 感知时间戳中删除时区。   |
| Timestamp.tzname                                             | 返回自我。                                                   |
| Timestamp.utcfromtimestamp(ts)                               | 从 POSIX 时间戳构造一个幼稚的 UTC 日期时间。                 |
| Timestamp.utcnow()                                           | 返回表示 UTC 日期和时间的新时间戳。                          |
| Timestamp.utcoffset                                          | 返回 self . tzinfo . utcoffset (自我)。                      |
| Timestamp.utctimetuple                                       | 返回 UTC 时间元组，与时间兼容。localtime ( )。               |
| Timestamp.weekday                                            | 返回日期所代表的星期几。                                     |
| **间隔**                                                     |                                                              |
| Interval                                                     | 实现一个区间的不可变对象，一个有界的切片状区间。             |
| **性能**                                                     |                                                              |
| Interval.closed                                              | 间隔是在左侧、右侧关闭，还是两者都关闭                       |
| Interval.closed_left                                         | 检查左侧间隔是否关闭。                                       |
| Interval.closed_right                                        | 检查右侧间隔是否关闭。                                       |
| Interval.left                                                | 左界间隔                                                     |
| Interval.length                                              | 返回间隔的长度                                               |
| Interval.mid                                                 | 返回间隔的中点                                               |
| Interval.open_left                                           | 检查左侧间隔是否打开。                                       |
| Interval.open_right                                          | 检查右侧间隔是否打开。                                       |
| Interval.right                                               | 右界间隔                                                     |
| **时间增量**                                                 |                                                              |
| Timedelta                                                    | 表示持续时间，即两个日期或时间之间的差值。                   |
| **性能**                                                     |                                                              |
| Timedelta.asm8                                               | 返回自己的 numpy timedelta 64 数组视图                       |
| Timedelta.components                                         | 返回一个名为 “类耦合” 的组件                                 |
| Timedelta.days                                               | 天数。                                                       |
| Timedelta.delta                                              | 返回以纳秒 (ns) 为单位的时间增量，以实现内部兼容性。         |
| Timedelta.freq                                               | -                                                            |
| Timedelta.is_populated                                       | -                                                            |
| Timedelta.max                                                | -                                                            |
| Timedelta.microseconds                                       | 微秒数 (> = 0 小于 1 秒)。                                   |
| Timedelta.min                                                | -                                                            |
| Timedelta.nanoseconds                                        | 返回纳秒数 (n)，其中 0≤n < 1 微秒。                          |
| Timedelta.resolution                                         | 返回一个字符串，表示我们拥有的最低分辨率                     |
| Timedelta.seconds                                            | 秒数 (> = 0 小于 1 天)。                                     |
| Timedelta.value                                              | -                                                            |
| Timedelta.view                                               | 阵列视图兼容性                                               |
| **方法**                                                     |                                                              |
| Timedelta.ceil                                               | 返回导致此解决方案的新 Timedelta CEI                         |
| Timedelta.floor                                              | 返回一个新的时间增量                                         |
| Timedelta.isoformat                                          | 将时间增量格式化为 ISO 8601 持续时间，如 P [n] Y [ n ] M [ n ] DT [ n ] H [ n ] M [ n ] S，其中 [ n ] S 由值替换。 |
| Timedelta.round                                              | 将时间增量舍入到指定的分辨率                                 |
| Timedelta.to_pytimedelta                                     | 返回一个实际的 datetime . timedelta 对象注意：如果有，我们将丢失纳秒分辨率 |
| Timedelta.to_timedelta64                                     | 返回一个精度为 “ns” 的 numpy . timedelta 64 对象             |
| Timedelta.total_seconds                                      | 时间增量的总持续时间 (以秒为单位) (精度为 ns )               |
| **频率**                                                     |                                                              |
| to_offset(freq)                                              | 从字符串或元组表示或 datetime . timedelta 对象返回 DateOffset 对象 |
| **窗户**                                                     |                                                              |
| **滚动对象由返回。点名：Pandas。DataFrame 滚动 ()，Pandas。Series 滚动 () 等。扩展对象由返回。扩大通话：Pandas。DataFrame. 扩展 ( )，Pandas。Series. 扩展 ( )，等等。EWM 对象由返回。ewm 电话：Pandas。DataFrame. ewm ( )，Pandas。Series. ewm ( )，等等。** |                                                              |
| **标准移动窗口功能**                                         |                                                              |
| Rolling.count()                                              | 窗口内任何非南观测的滚动计数。                               |
| Rolling.sum(*args, **kwargs)                                 | 计算给定 DataFrame 或 Series 的滚动和。                      |
| Rolling.mean(*args, **kwargs)                                | 计算值的滚动平均值。                                         |
| Rolling.median(**kwargs)                                     | 计算滚动中值。                                               |
| Rolling.var([ddof])                                          | 计算无偏滚动方差。                                           |
| Rolling.std([ddof])                                          | 计算轧制标准偏差。                                           |
| Rolling.min(*args, **kwargs)                                 | 计算滚动最小值。                                             |
| Rolling.max(*args, **kwargs)                                 | 滚动最大值                                                   |
| Rolling.corr([other, pairwise])                              | 滚动样本相关                                                 |
| Rolling.cov([other, pairwise, ddof])                         | 滚动样本协方差                                               |
| Rolling.skew(**kwargs)                                       | 无偏轧制偏度                                                 |
| Rolling.kurt(**kwargs)                                       | 计算无偏滚动峰度。                                           |
| Rolling.apply(func[, raw, args, kwargs])                     | 滚动功能适用                                                 |
| Rolling.aggregate(arg, *args, **kwargs)                      | 使用指定轴上的一个或多个操作聚合。                           |
| Rolling.quantile(quantile[, interpolation])                  | 滚动分位数。                                                 |
| Window.mean(*args, **kwargs)                                 | 计算值的窗口平均值。                                         |
| Window.sum(*args, **kwargs)                                  | 计算给定 DataFrame 或 Series 的窗口和。                      |
| **标准扩展窗口功能**                                         |                                                              |
| Expanding.count(**kwargs)                                    | 窗口内任何非南观测的扩展计数。                               |
| Expanding.sum(*args, **kwargs)                               | 计算给定 DataFrame 或 Series 的扩展和。                      |
| Expanding.mean(*args, **kwargs)                              | 计算值的展开平均值。                                         |
| Expanding.median(**kwargs)                                   | 计算膨胀中值。                                               |
| Expanding.var([ddof])                                        | 计算无偏扩展方差。                                           |
| Expanding.std([ddof])                                        | 计算扩展标准差。                                             |
| Expanding.min(*args, **kwargs)                               | 计算扩展最小值。                                             |
| Expanding.max(*args, **kwargs)                               | 膨胀最大值                                                   |
| Expanding.corr([other, pairwise])                            | 扩展样本相关性                                               |
| Expanding.cov([other, pairwise, ddof])                       | 扩展样本协方差                                               |
| Expanding.skew(**kwargs)                                     | 无偏膨胀偏度                                                 |
| Expanding.kurt(**kwargs)                                     | 计算无偏膨胀峰度。                                           |
| Expanding.apply(func[, raw, args, kwargs])                   | 扩展函数应用                                                 |
| Expanding.aggregate(arg, *args, **kwargs)                    | 使用指定轴上的一个或多个操作聚合。                           |
| Expanding.quantile(quantile[, interpolation])                | 扩展分位数。                                                 |
| **指数加权移动窗函数**                                       |                                                              |
| EWM.mean(*args, **kwargs)                                    | 指数加权移动平均                                             |
| EWM.std([bias])                                              | 指数加权移动标准开发                                         |
| EWM.var([bias])                                              | 指数加权移动方差                                             |
| EWM.corr([other, pairwise])                                  | 指数加权样本相关                                             |
| EWM.cov([other, pairwise, bias])                             | 指数加权样本协方差                                           |
| **GroupBy**                                                  |                                                              |
| **GroupBy 对象由 GroupBy 调用返回：Pandas。DataFrame. 群比 ()，Pandas。Series. groupby ()，等等。** |                                                              |
| **索引、迭代**                                               |                                                              |
| GroupBy.**iter**()                                           | 群比迭代器                                                   |
| GroupBy.groups                                               | dict {组名 -> 组标签}                                        |
| GroupBy.indices                                              | dict {组名 -> 组索引}                                        |
| GroupBy.get_group(name[, obj])                               | 使用提供的名称从组中构造 NDFrame                             |
| Grouper([key, level, freq, axis, sort])                      | groupby 允许用户为目标对象指定 groupby 指令                  |
| **功能应用**                                                 |                                                              |
| GroupBy.apply(func, *args, **kwargs)                         | 按组应用函数，并将结果组合在一起。                           |
| GroupBy.aggregate(func, *args, **kwargs)                     | -                                                            |
| GroupBy.transform(func, *args, **kwargs)                     | -                                                            |
| GroupBy.pipe(func, *args, **kwargs)                          | 将带有参数的函数 func 应用于此 groubby 对象，并返回函数的结果。 |
| **计算 / 描述统计**                                          |                                                              |
| GroupBy.all([skipna])                                        | 如果组中的所有值都是真实的，则返回 True，否则返回 False      |
| GroupBy.any([skipna])                                        | 如果组中的任何值是真实的，则返回 True，否则返回 False        |
| GroupBy.bfill([limit])                                       | 向后填充值                                                   |
| GroupBy.count()                                              | 计算组计数，不包括缺少的值                                   |
| GroupBy.cumcount([ascending])                                | 将每组中的每个项目编号为 0 到该组 - 1 的长度。               |
| GroupBy.ffill([limit])                                       | 向前填充这些值                                               |
| GroupBy.first(**kwargs)                                      | 先计算组值                                                   |
| GroupBy.head([n])                                            | 返回每个组的前 n 行。                                        |
| GroupBy.last(**kwargs)                                       | 计算最后一组值                                               |
| GroupBy.max(**kwargs)                                        | 计算组值的最大值                                             |
| GroupBy.mean(*args, **kwargs)                                | 计算组平均值，不包括缺少的值                                 |
| GroupBy.median(**kwargs)                                     | 计算组的中值，不包括缺少的值                                 |
| GroupBy.min(**kwargs)                                        | 计算组值最小值                                               |
| GroupBy.ngroup([ascending])                                  | 将每个组从 0 编号到组数 - 1。                                |
| GroupBy.nth(n[, dropna])                                     | 如果 n 是 int，则从每组中取第 n 行，如果 n 是 int 列表，则取行子集。 |
| GroupBy.ohlc()                                               | 计算值之和，不包括多个分组的缺失值，结果索引将是多索引       |
| GroupBy.prod(**kwargs)                                       | 计算组值乘积                                                 |
| GroupBy.rank([method, ascending, na_option, …])              | 提供每个组中的值的等级。                                     |
| GroupBy.pct_change([periods, fill_method, …])                | 计算每个值到组中先前条目的 pct _ change                      |
| GroupBy.size()                                               | 计算组大小                                                   |
| GroupBy.sem([ddof])                                          | 计算组平均值的标准误差，不包括缺失值                         |
| GroupBy.std([ddof])                                          | 计算组的标准差，不包括缺失值                                 |
| GroupBy.sum(**kwargs)                                        | 计算组值之和                                                 |
| GroupBy.var([ddof])                                          | 计算组的方差，不包括缺少的值                                 |
| GroupBy.tail([n])                                            | 返回每个组的最后 n 行                                        |
| **以下方法在 SeriesGroupBy 和 data framegroupby 对象中都可用，但可能略有不同，通常是因为 data framegroupby 版本通常允许指定 axis 参数，并且通常是指示是否将应用程序限制在特定数据类型的列的参数。** |                                                              |
| DataFrameGroupBy.agg(arg, *args, **kwargs)                   | 使用指定轴上的一个或多个操作聚合。                           |
| DataFrameGroupBy.all([skipna])                               | 如果组中的所有值都是真实的，则返回 True，否则返回 False      |
| DataFrameGroupBy.any([skipna])                               | 如果组中的任何值是真实的，则返回 True，否则返回 False        |
| DataFrameGroupBy.bfill([limit])                              | 向后填充值                                                   |
| DataFrameGroupBy.corr                                        | 计算列的成对相关性，不包括 NA /null 值                       |
| DataFrameGroupBy.count()                                     | 计算组计数，不包括缺少的值                                   |
| DataFrameGroupBy.cov                                         | 计算列的成对协方差，不包括 NA /null 值。                     |
| DataFrameGroupBy.cummax([axis])                              | 每个组的累计最大值                                           |
| DataFrameGroupBy.cummin([axis])                              | 每组的累计最小值                                             |
| DataFrameGroupBy.cumprod([axis])                             | 每组累积产品                                                 |
| DataFrameGroupBy.cumsum([axis])                              | 每组累计金额                                                 |
| DataFrameGroupBy.describe(**kwargs)                          | 生成描述性统计数据，总结数据集分布的中心趋势、分散和形状，不包括 NaN 值。 |
| DataFrameGroupBy.diff                                        | 元素的第一离散差。                                           |
| DataFrameGroupBy.ffill([limit])                              | 向前填充这些值                                               |
| DataFrameGroupBy.fillna                                      | 使用指定的方法填写 NA / NaN 值                               |
| DataFrameGroupBy.filter(func[, dropna])                      | 返回 DataFrame 的副本，不包括不满足 func 指定的布尔条件的组中的元素。 |
| DataFrameGroupBy.hist                                        | 制作 DataFrame 的直方图。                                    |
| DataFrameGroupBy.idxmax                                      | 返回请求轴上首次出现最大值的索引。                           |
| DataFrameGroupBy.idxmin                                      | 返回请求轴上第一次出现最小值的索引。                         |
| DataFrameGroupBy.mad                                         | 返回请求轴值的平均绝对偏差                                   |
| DataFrameGroupBy.pct_change([periods, …])                    | 计算每个值到组中先前条目的 pct _ change                      |
| DataFrameGroupBy.plot                                        | 实现的类。群组依据物件的出图属性                             |
| DataFrameGroupBy.quantile                                    | 在请求轴上给定分位数的返回值，la numpy . 百分位。            |
| DataFrameGroupBy.rank([method, ascending, …])                | 提供每个组中的值的等级。                                     |
| DataFrameGroupBy.resample(rule, *args, **kwargs)             | 使用 TimeGrouper 时提供 Resampling 返回带有我们的 Resampling 器的新 grouper |
| DataFrameGroupBy.shift([periods, freq, axis])                | 每组按时段移动观察                                           |
| DataFrameGroupBy.size()                                      | 计算组大小                                                   |
| DataFrameGroupBy.skew                                        | 返回由 N - 1 归一化的请求轴上的无偏歪斜                      |
| DataFrameGroupBy.take                                        | 沿轴返回给定位置索引中的元素。                               |
| DataFrameGroupBy.tshift                                      | 移动时间索引，使用索引的频率 (如果可用)。                    |
| **以下方法仅适用于 SeriesGroupBy 对象。**                    |                                                              |
| SeriesGroupBy.nlargest                                       | 返回最大的 n 个元素。                                        |
| SeriesGroupBy.nsmallest                                      | 返回最小的 n 个元素。                                        |
| SeriesGroupBy.nunique([dropna])                              | 返回组中唯一元素的数量                                       |
| SeriesGroupBy.unique                                         | 返回 Series 对象的唯一值。                                   |
| SeriesGroupBy.value_counts([normalize, …])                   | -                                                            |
| SeriesGroupBy.is_monotonic_increasing                        | 如果对象中的值是单调递增的，则返回 boolean                   |
| SeriesGroupBy.is_monotonic_decreasing                        | 如果对象中的值是单调递减的，则返回 boolean                   |
| **以下方法仅适用于 DataFrameGroupBy 对象。**                 |                                                              |
| DataFrameGroupBy.corrwith                                    | 计算两个 DataFrame 对象的行或列之间的成对相关性。            |
| DataFrameGroupBy.boxplot([subplots, column, …])              | 根据 DataFrame 组制作方框图。                                |
| **Resampling**                                               |                                                              |
| **Resampling 对象通过 Resampling 调用返回：Pandas。DataFrame.Resampling ()，Pandas。Series. 重新取样 ()。** |                                                              |
| **索引、迭代**                                               |                                                              |
| Resampler.**iter**()                                         | 群比迭代器                                                   |
| Resampler.groups                                             | dict {组名 -> 组标签}                                        |
| Resampler.indices                                            | dict {组名 -> 组索引}                                        |
| Resampler.get_group(name[, obj])                             | 使用提供的名称从组中构造 NDFrame                             |
| **功能应用**                                                 |                                                              |
| Resampler.apply(arg, *args, **kwargs)                        | 使用指定轴上的一个或多个操作聚合。                           |
| Resampler.aggregate(arg, *args, **kwargs)                    | 使用指定轴上的一个或多个操作聚合。                           |
| Resampler.transform(arg, *args, **kwargs)                    | 调用函数，在每个组上生成一个类似索引的 Series，并返回一个带有转换值的 Series |
| Resampler.pipe(func, *args, **kwargs)                        | 将带有参数的函数 func 应用于此重新采样器对象，并返回函数的结果。 |
| **上采样**                                                   |                                                              |
| Resampler.ffill([limit])                                     | 向前填充这些值                                               |
| Resampler.backfill([limit])                                  | 在重新采样的数据中向后填充新的缺失值。                       |
| Resampler.bfill([limit])                                     | 在重新采样的数据中向后填充新的缺失值。                       |
| Resampler.pad([limit])                                       | 向前填充这些值                                               |
| Resampler.nearest([limit])                                   | 从中心开始用最近邻填充值                                     |
| Resampler.fillna(method[, limit])                            | 填充上采样引入的缺失值。                                     |
| Resampler.asfreq([fill_value])                               | 返回新频率的值，本质上是重新索引                             |
| Resampler.interpolate([method, axis, limit, …])              | 根据不同的方法插值。                                         |
| **计算 / 描述统计**                                          |                                                              |
| Resampler.count([_method])                                   | 计算组计数，不包括缺少的值                                   |
| Resampler.nunique([_method])                                 | 返回组中唯一元素的数量                                       |
| Resampler.first([_method])                                   | 先计算组值                                                   |
| Resampler.last([_method])                                    | 计算最后一组值                                               |
| Resampler.max([_method])                                     | 计算组值的最大值                                             |
| Resampler.mean([_method])                                    | 计算组平均值，不包括缺少的值                                 |
| Resampler.median([_method])                                  | 计算组的中值，不包括缺少的值                                 |
| Resampler.min([_method])                                     | 计算组值最小值                                               |
| Resampler.ohlc([_method])                                    | 计算值之和，不包括多个分组的缺失值，结果索引将是多索引       |
| Resampler.prod([_method, min_count])                         | 计算组值乘积                                                 |
| Resampler.size()                                             | 计算组大小                                                   |
| Resampler.sem([_method])                                     | 计算组平均值的标准误差，不包括缺失值                         |
| Resampler.std([ddof])                                        | 计算组的标准差，不包括缺失值                                 |
| Resampler.sum([_method, min_count])                          | 计算组值之和                                                 |
| Resampler.var([ddof])                                        | 计算组的方差，不包括缺少的值                                 |
| **风格**                                                     |                                                              |
| **styler 对象由 Pandas 返回**                                |                                                              |
| **样式构造器**                                               |                                                              |
| Styler(data[, precision, table_styles, …])                   | 使用 HTML 和 CSS 帮助根据数据设置 DataFrame 或 Series 的样式。 |
| Styler.from_custom_template(searchpath, name)                | 工厂函数，用于使用自定义模板和 Jinja 环境创建 Styler 子类。  |
| **样式属性**                                                 |                                                              |
| Styler.env                                                   | -                                                            |
| Styler.template                                              | -                                                            |
| Styler.loader                                                | -                                                            |
| **样式应用**                                                 |                                                              |
| Styler.apply(func[, axis, subset])                           | 应用函数列、行或表 wase，用结果更新 HTML 表示。              |
| Styler.applymap(func[, subset])                              | 以元素方式应用函数，用结果更新 HTML 表示。                   |
| Styler.where(cond, value[, other, subset])                   | 以元素方式应用函数，用根据函数返回值选择的样式更新 HTML 表示。 |
| Styler.format(formatter[, subset])                           | 格式化单元格的文本显示值。                                   |
| Styler.set_precision(precision)                              | 设置用于渲染的精度。                                         |
| Styler.set_table_styles(table_styles)                        | 在样式器上设置表格样式。                                     |
| Styler.set_table_attributes(attributes)                      | 设置表属性。                                                 |
| Styler.set_caption(caption)                                  | 在样式器上设置标题                                           |
| Styler.set_properties([subset])                              | 为每个单元格设置一个或多个非数据相关属性的便捷方法。         |
| Styler.set_uuid(uuid)                                        | 设置样式器的 uuid。                                          |
| Styler.clear()                                               | “重置” 样式器，删除以前应用的任何样式。                      |
| **内置样式**                                                 |                                                              |
| Styler.highlight_max([subset, color, axis])                  | 通过阴影化背景来突出显示最大值                               |
| Styler.highlight_min([subset, color, axis])                  | 通过阴影化背景来突出显示最小值                               |
| Styler.highlight_null([null_color])                          | 为缺少的值着色背景 null _ color。                            |
| Styler.background_gradient([cmap, low, …])                   | 根据每列 (可选行) 中的数据为背景上色。                       |
| Styler.bar([subset, axis, color, width, align])              | 将背景颜色标记为每列中的值。                                 |
| **样式导出和导入**                                           |                                                              |
| Styler.render(**kwargs)                                      | 将构建的样式渲染为 HTML                                      |
| Styler.export()                                              | 导出要应用于当前样式的样式。                                 |
| Styler.use(styles)                                           | 设置当前样式器上的样式，可能使用样式器中的样式。导出         |
| Styler.to_excel(excel_writer[, sheet_name, …])               | 将样式写入 excel 工作表                                      |
| **绘图**                                                     |                                                              |
| **Pandas 绘图模块包含以下功能。**                            |                                                              |
| andrews_curves(frame, class_column[, ax, …])                 | 生成 Andrews 曲线的 matplotlib 图，用于可视化多变量数据集群。 |
| bootstrap_plot(series[, fig, size, samples])                 | 均值、中值和中值统计的自举图。                               |
| deregister_matplotlib_converters()                           | 移除 Pandas 的格式化程序和转换器                             |
| lag_plot(series[, lag, ax])                                  | 时间 Series 的滞后图。                                       |
| parallel_coordinates(frame, class_column[, …])               | 平行坐标绘图。                                               |
| radviz(frame, class_column[, ax, color, …])                  | 在 2D 中绘制多维数据集。                                     |
| register_matplotlib_converters([explicit])                   | 用 matplotlib 注册 Pandas 格式化程序和转换器                 |
| scatter_matrix(frame[, alpha, figsize, ax, …])               | 绘制散点图矩阵。                                             |
| **通用功能**                                                 |                                                              |
| **使用选项**                                                 |                                                              |
| describe_option(pat[, _print_desc])                          | 打印一个或多个已注册选项的说明。                             |
| reset_option(pat)                                            | 将一个或多个选项重置为默认值。                               |
| get_option(pat)                                              | 检索指定选项的值。                                           |
| set_option(pat, value)                                       | 设置指定选项的值。                                           |
| option_context(*args)                                        | 上下文管理器在 with 语句上下文中临时设置选项。               |
| **测试功能**                                                 |                                                              |
| testing.assert_frame_equal(left, right[, …])                 | 检查左右 DataFrame 是否相等。                                |
| testing.assert_series_equal(left, right[, …])                | 检查左右 Series 是否相等。                                   |
| testing.assert_index_equal(left, right[, …])                 | 检查左右索引是否相等。                                       |
| **例外和警告**                                               |                                                              |
| errors.DtypeWarning                                          | 从文件读取列中的不同 dtypes 时发出警告。                     |
| errors.EmptyDataError                                        | 遇到空数据或标头时在 PD . read _ CSV 中引发的异常 (由 C 和 Python 引擎引发)。 |
| errors.OutOfBoundsDatetime                                   | -                                                            |
| errors.ParserError                                           | 由 PD . read _ CSV 中遇到的错误引发的异常。                  |
| errors.ParserWarning                                         | 读取不使用默认 “c” 分析器的文件时发出警告。                  |
| errors.PerformanceWarning                                    | 可能影响性能时发出警告。                                     |
| errors.UnsortedIndexError                                    | 尝试获取多索引切片时引发错误，并且该索引尚未进行词法排序。   |
| errors.UnsupportedFunctionCall                               | 尝试在 Pandas 对象上调用 numpy 函数时引发异常，但该对象不支持该函数 |
| **数据类型相关功能**                                         |                                                              |
| api.types.union_categoricals(to_union[, …])                  | 组合类列表类、联合类。                                       |
| api.types.infer_dtype                                        | 有效推断传递的 val 或类似列表的值数组的类型。                |
| api.types.pandas_dtype(dtype)                                | 将输入转换为仅 Pandasdtype 对象或 numpy dtype 对象。         |
| **型内省**                                                   |                                                              |
| api.types.is_bool_dtype(arr_or_dtype)                        | 检查所提供的数组或 dtype 是否为布尔 dtype。                  |
| api.types.is_categorical_dtype(arr_or_dtype)                 | 检查数组状或 dtype 是否属于分类 dtype。                      |
| api.types.is_complex_dtype(arr_or_dtype)                     | 检查所提供的数组或 dtype 是否为复杂的 dtype。                |
| api.types.is_datetime64_any_dtype(arr_or_dtype)              | 检查提供的数组或 dtype 是否为 datetime64 dtype。             |
| api.types.is_datetime64_dtype(arr_or_dtype)                  | 检查阵列状或 dtype 是否为 datetime64 dtype。                 |
| api.types.is_datetime64_ns_dtype(arr_or_dtype)               | 检查所提供的数组或 dtype 是否为 datetime64 [ns] dtype。      |
| api.types.is_datetime64tz_dtype(arr_or_dtype)                | 检查阵列状或 dtype 是否为 DatetimeTZDtype dtype。            |
| api.types.is_extension_type(arr)                             | 检查类数组是否属于 Pandas 扩展类实例。                       |
| api.types.is_float_dtype(arr_or_dtype)                       | 检查所提供的数组或 dtype 是否为浮点 dtype。                  |
| api.types.is_int64_dtype(arr_or_dtype)                       | 检查提供的数组或 dtype 是否为 int64 dtype。                  |
| api.types.is_integer_dtype(arr_or_dtype)                     | 检查所提供的数组或 dtype 是否为整数 dtype。                  |
| api.types.is_interval_dtype(arr_or_dtype)                    | 检查阵列状或 dtype 是否为间隔 dtype。                        |
| api.types.is_numeric_dtype(arr_or_dtype)                     | 检查所提供的数组或 dtype 是否为数字 dtype。                  |
| api.types.is_object_dtype(arr_or_dtype)                      | 检查阵列状或 dtype 是否为物件 dtype。                        |
| api.types.is_period_dtype(arr_or_dtype)                      | 检查数组类型或 dtype 是否为周期 dtype。                      |
| api.types.is_signed_integer_dtype(arr_or_dtype)              | 检查所提供的数组或 dtype 是否为带符号整数 dtype。            |
| api.types.is_string_dtype(arr_or_dtype)                      | 检查提供的数组或 dtype 是否为字符串 dtype。                  |
| api.types.is_timedelta64_dtype(arr_or_dtype)                 | 检查阵列状或 dtype 是否为 timedelta 64 dtype。               |
| api.types.is_timedelta64_ns_dtype(arr_or_dtype)              | 检查所提供的数组或 dtype 是否为 timedelta 64 [ns] dtype。    |
| api.types.is_unsigned_integer_dtype(arr_or_dtype)            | 检查所提供的数组或 dtype 是否为无符号整数 dtype。            |
| api.types.is_sparse(arr)                                     | 检查阵列状是否为 Pandas 稀疏阵列。                           |
| **反复反省**                                                 |                                                              |
| api.types.is_dict_like(obj)                                  | 检查对象是否像 dict 一样。                                   |
| api.types.is_file_like(obj)                                  | 检查对象是否为类文件对象。                                   |
| api.types.is_list_like(obj)                                  | 检查对象是否类似列表。                                       |
| api.types.is_named_tuple(obj)                                | 检查对象是否为命名元组。                                     |
| api.types.is_iterator(obj)                                   | 检查对象是否是迭代器。                                       |
| **标量内省**                                                 |                                                              |
| api.types.is_bool                                            | -                                                            |
| api.types.is_categorical(arr)                                | 检查类数组是否是分类实例。                                   |
| api.types.is_complex                                         | -                                                            |
| api.types.is_datetimetz(arr)                                 | 检查阵列状是否为 dtype 中含有时区元件的日期时间阵列状。      |
| api.types.is_float                                           | -                                                            |
| api.types.is_hashable(obj)                                   | 如果哈希 (obj) 成功，则返回 True，否则返回 False。           |
| api.types.is_integer                                         | -                                                            |
| api.types.is_interval                                        | -                                                            |
| api.types.is_number(obj)                                     | 检查对象是否为数字。                                         |
| api.types.is_period(arr)                                     | 检查阵列状是否为周期性索引。                                 |
| api.types.is_re(obj)                                         | 检查对象是否为 regex 模式实例。                              |
| api.types.is_re_compilable(obj)                              | 检查对象是否可以编译成 regex 模式实例。                      |
| api.types.is_scalar                                          | 如果给定值是标量，则返回 True。                              |
| **延长**                                                     |                                                              |
| **这些主要是为图书馆的作者打算扩展 Pandas 的对象。**         |                                                              |
| api.extensions.register_dataframe_accessor(name)             | 在 DataFrame 对象上注册自定义访问者。                        |
| api.extensions.register_series_accessor(name)                | 在 Series 对象上注册自定义访问者。                           |
| api.extensions.register_index_accessor(name)                 | 在索引对象上注册自定义访问者。                               |
| api.extensions.ExtensionDtype                                | 自定义数据类型，要与扩展数组配对。                           |
| api.extensions.ExtensionArray                                | 自定义一维数组类型的抽象基类。                               |

