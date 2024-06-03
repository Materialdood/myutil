package helper

import (
	"time"
	"fmt"
	"net/http"
	"net/http/httputil"
	"encoding/json"
	"github.com/PuerkitoBio/goquery"
	"os"
)

// convertTimestampToDatetime converts a Unix timestamp to a formatted date-time string
func ConvertTimestampToDatetime(timestamp int64) string {
	t := time.Unix(timestamp, 0)
	formattedTime := t.Format("2006-01-02 15:04:05")
	return formattedTime
}

func CalculateDeltaTime(timestamp1, timestamp2 int64) time.Duration {
	// Convert timestamps to time.Time
	time1 := time.Unix(timestamp1, 0)
	time2 := time.Unix(timestamp2, 0)

	// Calculate the delta time
	delta := time2.Sub(time1)

	return delta
}
