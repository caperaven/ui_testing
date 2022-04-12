def set_error(results, step_name, message):
    results[step_name] = message
    results["summary"]["success"] = False
    results["summary"]["error_count"] = results["summary"]["error_count"] + 1
