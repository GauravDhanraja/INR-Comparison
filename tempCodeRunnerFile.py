    data['Currency Strength'] = 1 / data['1.00 INR']

    # Plotting
    plt.figure(figsize=(12, 8))

    # Plot currency strength
    plt.barh(data['Country'], data['Currency Strength'], color='green', alpha=0.7)

    plt.xlabel('Currency Strength (relative to 1.00 INR)')
    plt.title('Currency Strength Relative to INR')
    plt.gca().invert_yaxis()  # Invert y-axis to display countries from top to bottom
    plt.tight_layout()

    plt.show()