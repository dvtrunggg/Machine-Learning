# phân tích 1 biến
def continuous_univariate_analysis(f):
    print("1\ Describe: \n", f.describe(), "\n")
    print("2\ Meadian: ", f.median())
    # print("3\ Mode: ", f.mode)
    print("4\ Range: ", f.values.ptp())
    print("5\ Variance: ", f.var())
    print("6\ Số NaN: ", f.isnull().sum())
    print(f"Number of unique values: {df[col].nunique()}")
    print("7\ \tQ1 = ", np.quantile(f, 0.25))
    print("   \tQ3 = ", np.quantile(f, 0.75))
    print("   \tIQR = ", iqr(f))

    print("8\ Skew: ", f.skew())
    if f.skew() > 0:
        print("Phân phối lệch phải")
    elif f.skew() == 0:
        print("Phân phối đối xứng")
    else:
        print("Phân phối lệch trái")

    print("9\ Kurtosis: ", f.kurtosis())
    if f.kurtosis() > 0:
        print("Phân phối nhọn hơn pp chuẩn")
    elif f.kurtosis() == 0:
        print("Phân phối đối xứng")
    else:
        print("Phân phối bẹt hơn pp chuẩn")
        
def visualize_boxplot(f):
    plt.boxplot(f)
    plt.show()
    
def find_outliers(f):
    Q1 = np.quantile(f, 0.25)
    Q3 = np.quantile(f, 0.75)
    IQR = Q3 - Q1
    
    # số lượng outliers
    num_outliers = len(f[(f > Q3 + 1.5 * IQR) | (f < Q1 - 1.5 * IQR)])
    
    # tỉ lệ outliers so với mẫu
    ratio = (num_outliers / f.shape[0])
                       
    print('Số lượng outliers: ', num_outliers)
    print('Tỉ lệ outliers so với mẫu', ratio)


# phân tích 2 biến

def continuous_multivariate_analysis(dataset):
    df_corr = dataset.corr()
    print(df_corr)
    
    # Visualisation
    sns.pairplot(dataset)
    plt.show()
