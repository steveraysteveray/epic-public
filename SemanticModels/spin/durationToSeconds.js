/**
 * DurationStrToMS
 * input : duration as String (e.g. "PT30M")
 * output :  duration is milliseconds
 */

function DurationStrToMS(durationString) {

	var seconds = 0;
	var minutes = durationString.match(/(\d+)\s*M/);
	var days = durationString.match(/(\d+)\s*D/);
	var hours = durationString.match(/(\d+)\s*H/);
	var minutes = durationString.match(/(\d+)\s*M/);
	if (days) { 
		seconds += parseInt(days[1])*86400; 
	}
	if (hours) { 
		seconds += parseInt(hours[1])*3600; 
	}
	if (minutes) { 
		seconds += parseInt(minutes[1])*60; 
	}

	return seconds*1000;
}