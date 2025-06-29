import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import axios from 'axios';
import { Chart } from 'react-chartjs-2';
import 'chart.js/auto';

const AnalyticsChart = ({ endpoint, chartType, options }) => {
  const { t } = useTranslation();
  const [chartData, setChartData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(endpoint);
        setChartData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchData();
  }, [endpoint]);

  if (loading) {
    return <div>{t('loading')}</div>;
  }

  if (error) {
    return <div>{t('error')}</div>;
  }

  return (
    <div aria-live="polite" aria-busy={loading}>
      <Chart type={chartType} data={chartData} options={options} />
    </div>
  );
};

AnalyticsChart.propTypes = {
  endpoint: PropTypes.string.isRequired,
  chartType: PropTypes.oneOf(['line', 'bar', 'radar', 'pie', 'doughnut', 'polarArea', 'bubble', 'scatter']).isRequired,
  options: PropTypes.object,
};

AnalyticsChart.defaultProps = {
  options: {},
};

export default AnalyticsChart;