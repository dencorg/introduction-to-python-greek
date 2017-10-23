#!/usr/bin/env python
# -*- coding: utf-8 -*-

# εισαγωγή απαραίτητων modules
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# κανονική κατανομή

# μέση τιμή, διακύμανση
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# δεδομένα ιστογράμματος
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# συνάρτηση πυκνότητας πιθανότητας
y = mlab.normpdf(bins, mu, sigma)

# πρόσθεσε τη γραμμή
l = plt.plot(bins, y, 'r--', linewidth=1)

# δημιουργία γραφήματος
plt.ylabel('Πιθανότητα')
plt.title('Ιστόγραμμα με mu={}, sigma={}'.format(mu, sigma))
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()