export default
{
    "queryDb": {
        
        "minWorkingTime": `SELECT union_reporting.project.name as PROJECT, 
        union_reporting.test.name as TEST, 
        (union_reporting.test.end_time-union_reporting.test.start_time) AS MIN_WORKING_TIME 
        FROM union_reporting.test 
        JOIN union_reporting.project 
        ON union_reporting.test.project_id = union_reporting.project.id 
        ORDER BY PROJECT, TEST DESC`,

        "testsCount": `SELECT name as PROJECT, TEST_COUNT 
        FROM (SELECT union_reporting.test.project_id AS PROJECT_ID, COUNT(DISTINCT union_reporting.test.name) AS TEST_COUNT FROM union_reporting.test GROUP BY PROJECT_ID) AS Tab1 
        JOIN (SELECT * FROM union_reporting.project) AS Tab2 
        ON Tab1.PROJECT_ID=Tab2.id`,

        "testsDate": `SELECT union_reporting.project.name as PROJECT, union_reporting.test.name as TEST, union_reporting.test.start_time AS DATE_TIME 
        FROM union_reporting.test 
        JOIN union_reporting.project 
        ON union_reporting.test.project_id = union_reporting.project.id 
        WHERE union_reporting.test.start_time >= '2015-11-01 00:00:00' 
        ORDER BY PROJECT, TEST DESC`,

        "browserCount": `SELECT count(union_reporting.test.name) as BROWSERS 
        FROM union_reporting.test 
        WHERE union_reporting.test.browser = 'chrome' 
        UNION ALL 
        SELECT count(union_reporting.test.name) 
        FROM union_reporting.test 
        WHERE union_reporting.test.browser = 'firefox' 
        GROUP BY browser`
    }
}