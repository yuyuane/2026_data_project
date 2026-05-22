CREATE TABLE jobs (
    id BIGSERIAL PRIMARY KEY,

    job_uid VARCHAR(255) UNIQUE NOT NULL,

    name VARCHAR(500) NOT NULL,

    publish_time TIMESTAMP,

    company VARCHAR(255),

    company_detail TEXT,

    followers INTEGER DEFAULT 0,

    apply_type SMALLINT DEFAULT 1,

    employment_type SMALLINT DEFAULT 1,

    work_mode SMALLINT DEFAULT 1,

    work_place VARCHAR(255),

    applicants INTEGER DEFAULT 0,

    detail TEXT,

    source SMALLINT NOT NULL,

    source_url TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);