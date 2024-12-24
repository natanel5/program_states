def check_alerts(alerts):
    """
    Checks the alerts in the system and returns a report.

    Parameters:
        alerts (list of dict): A list of alerts, where each alert is represented as a dictionary.
                               Each alert dictionary should have the following keys:
                               - 'id': Unique identifier for the alert.
                               - 'message': The message describing the alert.
                               - 'severity': Severity level of the alert ('low', 'medium', 'high').
                               - 'timestamp': The time the alert was generated.

    Returns:
        dict: A dictionary containing the number of alerts by severity and a list of high-severity alerts.
    """
    if not isinstance(alerts, list):
        raise ValueError("Alerts should be a list of dictionaries.")

    severity_count = {'low': 0, 'medium': 0, 'high': 0}
    high_severity_alerts = []

    for alert in alerts:
        if not all(key in alert for key in ('id', 'message', 'severity', 'timestamp')):
            raise ValueError("Each alert must contain 'id', 'message', 'severity', and 'timestamp' keys.")

        severity = alert.get('severity').lower()
        if severity not in severity_count:
            raise ValueError(f"Invalid severity level: {severity}")

        severity_count[severity] += 1

        if severity == 'high':
            high_severity_alerts.append(alert)

    return {
        'severity_count': severity_count,
        'high_severity_alerts': high_severity_alerts
    }

# Example usage:
alerts = [
    {'id': 1, 'message': 'CPU usage is high', 'severity': 'high', 'timestamp': '2024-12-22T10:00:00Z'},
    {'id': 2, 'message': 'Disk space running low', 'severity': 'medium', 'timestamp': '2024-12-22T11:00:00Z'},
    {'id': 3, 'message': 'Memory usage is normal', 'severity': 'low', 'timestamp': '2024-12-22T12:00:00Z'},
    {'id': 4, 'message': 'Network latency detected', 'severity': 'high', 'timestamp': '2024-12-22T13:00:00Z'}
]

report = check_alerts(alerts)
print(report)
