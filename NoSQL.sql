CREATE TABLE public.products
(
    data json,
    CONSTRAINT validate_id CHECK (((data ->> 'id'::text)::integer) >= 1 AND (data ->> 'id'::text) IS NOT NULL),
    CONSTRAINT validate_name CHECK (length(data ->> 'name'::text) > 0 AND (data ->> 'name'::text) IS NOT NULL),
    CONSTRAINT validate_description CHECK (length(data ->> 'description'::text) > 0 AND (data ->> 'description'::text) IS NOT NULL),
    CONSTRAINT validate_price CHECK (((data ->> 'price'::text)::numeric) >= 0.0 AND (data ->> 'price'::text) IS NOT NULL),
    CONSTRAINT validate_currency CHECK ((data ->> 'currency'::text) = 'dollars'::text AND (data ->> 'currency'::text) IS NOT NULL),
    CONSTRAINT validate_in_stock CHECK (((data ->> 'in_stock'::text)::integer) >= 0 AND (data ->> 'in_stock'::text) IS NOT NULL)
)

TABLESPACE pg_default;

ALTER TABLE public.products
    OWNER to postgres;
-- Index: i_products_ids

-- DROP INDEX public.i_products_ids;

CREATE INDEX i_products_ids
    ON public.products USING btree
    (((data ->> 'id'::text)::integer) ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: i_products_in_stock

-- DROP INDEX public.i_products_in_stock;

CREATE INDEX i_products_in_stock
    ON public.products USING btree
    (((data ->> 'in_stock'::text)::integer) ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: ui_products_id

-- DROP INDEX public.ui_products_id;

CREATE UNIQUE INDEX ui_products_id
    ON public.products USING btree
    ((data ->> 'id'::text) COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
