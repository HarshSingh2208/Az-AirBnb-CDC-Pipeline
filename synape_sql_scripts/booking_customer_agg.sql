CREATE PROCEDURE airbnb.BookingAggregation
AS
BEGIN
    TRUNCATE TABLE airbnb.BookingCustomerAggregation;

    INSERT INTO airbnb.BookingCustomerAggregation
    SELECT 
        c.country,
        COUNT_BIG(*) AS total_bookings,
        SUM(ISNULL(b.amount, 0)) AS total_amount,
        MAX(b.booking_date) AS last_booking_date
    FROM 
        airbnb.bookings_fact b
    JOIN 
        airbnb.customer_dim c ON b.customer_id = c.customer_id
    GROUP BY 
        c.country;
END;

EXEC [airbnb].[BookingAggregation];

select * from airbnb.BookingCustomerAggregation;