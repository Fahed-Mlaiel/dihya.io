import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';

const NotificationItem = ({ message, type }) => {
  const { t } = useTranslation();

  return (
    <div className={`notification-item ${type}`}>
      {t(message)}
    </div>
  );
};

NotificationItem.propTypes = {
  message: PropTypes.string.isRequired,
  type: PropTypes.oneOf(['info', 'success', 'warning', 'error']).isRequired,
};

const NotificationCenter = ({ socket }) => {
  const [notifications, setNotifications] = useState([]);
  const { t } = useTranslation();

  useEffect(() => {
    if (socket) {
      socket.on('notification', (notification) => {
        setNotifications((prevNotifications) => [...prevNotifications, notification]);
      });
    }

    return () => {
      if (socket) {
        socket.off('notification');
      }
    };
  }, [socket]);

  return (
    <div aria-live="polite" aria-atomic="true" className="notification-center">
      <h2 className="visually-hidden">{t('notifications')}</h2>
      {notifications.map((notification, index) => (
        <NotificationItem key={index} {...notification} />
      ))}
    </div>
  );
};

NotificationCenter.propTypes = {
  socket: PropTypes.object.isRequired,
};

export default NotificationCenter;