{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPPov6/3jOhIp84+virqQjG",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/HrishikeshShinde3/python_pandas/blob/my_practice_branch/pandas.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bOzTcHLewZfP",
        "outputId": "364accbc-4efa-418e-c33a-044c10c95f27"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Single Column selected from Dataset\n",
            "Name\n",
            "Avery Bradley    25\n",
            "Jae Crowder      25\n",
            "John Holland     27\n",
            "R.J. Hunter      22\n",
            "Jonas Jerebko    29\n",
            "Amir Johnson     29\n",
            "Jordan Mickey    21\n",
            "Kelly Olynyk     25\n",
            "Terry Rozier     22\n",
            "Marcus Smart     22\n",
            "Name: Age, dtype: int64\n"
          ]
        }
      ],
      "source": [
        "\n",
        "import pandas as pd\n",
        "\n",
        "data = pd.read_csv(\"/nba.csv\", index_col=\"Name\")\n",
        "\n",
        "\n",
        "first = data[\"Age\"]\n",
        "print(\"\\nSingle Column selected from Dataset\")\n",
        "print(first.head(10))"
      ]
    }
  ]
}