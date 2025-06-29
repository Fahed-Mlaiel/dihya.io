import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import { useTranslation } from 'react-i18next';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const AnalyticsWidget = ({ endpoint, chartKey, chartValue }) => {
  const { t } = useTranslation();
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(endpoint);
        setData(response.data);
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
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
        <XAxis dataKey={chartKey} />
        <YAxis />
        <Tooltip />
        <Bar dataKey={chartValue} fill="#8884d8" />
      </BarChart>
    </ResponsiveContainer>
  );
};

AnalyticsWidget.propTypes = {
  endpoint: PropTypes.string.isRequired,
  chartKey: PropTypes.string.isRequired,
  chartValue: PropTypes.string.isRequired,
};

export default AnalyticsWidget;